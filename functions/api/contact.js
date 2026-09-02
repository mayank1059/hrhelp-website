// Cloudflare Pages Function — proxies form submissions to WordPress REST API
// Bypasses CORS and attempts to bypass Mod Security with proper headers

// The contact form's placeholder option. It is disabled in the markup, so this
// is only defence in depth for cached pages that still submit it as a topic.
const TOPIC_PLACEHOLDER = 'Select a topic...';

function cleanTopic(topic) {
  if (typeof topic !== 'string') return '';
  const trimmed = topic.trim();
  return trimmed === TOPIC_PLACEHOLDER ? '' : trimmed;
}

// The forms collect UTM parameters and the referrer. The CRM intake has no
// columns for them, so they ride along as a final line of the message.
function originLine(body) {
  const parts = [];
  for (const key of ['utm_source', 'utm_medium', 'utm_campaign', 'referrer']) {
    const value = typeof body[key] === 'string' ? body[key].trim() : '';
    if (value) parts.push(key + '=' + value);
  }
  if (!parts.length) return '';
  return ('Herkomst: ' + parts.join(', ')).slice(0, 300);
}

// Copy of the submission into the CRM at client.hrhelp.nl.
// Never throws: resolves true only when the CRM accepted the lead.
async function sendToCrm(context, body) {
  const secret = context.env && context.env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM intake skipped/failed:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return false;
  }

  const origin = originLine(body);
  const message = origin
    ? (body.message ? body.message + '\n\n' + origin : origin)
    : body.message;

  const lead = {
    name: body.name,
    email: body.email,
    company: body.company,
    phone: body.phone,
    // The whitepaper forms send no topic but do send a source label
    // ("Whitepaper Download"); without it a guide download is
    // indistinguishable from a contact lead in the CRM.
    topic: cleanTopic(body.topic) || body.source,
    message,
  };
  // The raw form label, kept alongside the legacy `topic` fallback above.
  if (body.source) lead.channel = body.source;
  // The CRM uses the same url_confirm name for its own honeypot. Nothing reaches
  // here with it filled — onRequestPost short-circuits first — but passing it
  // verbatim means the CRM's guard still catches anything that ever slips past.
  if (typeof body.url_confirm === 'string' && body.url_confirm) lead.url_confirm = body.url_confirm;

  try {
    const res = await fetch('https://client.hrhelp.nl/api/leads/intake', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-intake-secret': secret,
      },
      body: JSON.stringify(lead),
    });
    if (!res.ok) {
      console.log('CRM intake skipped/failed:', 'status ' + res.status);
      return false;
    }
    return true;
  } catch (error) {
    console.log('CRM intake skipped/failed:', error.message);
    return false;
  }
}

// Forward to WordPress, which files the lead in FluentCRM and emails the team.
// Never throws: resolves true only when WordPress answered with a JSON success.
async function sendToWordPress(context, body) {
  const headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    // Browser-like header to get past Mod Security
    'User-Agent': 'Mozilla/5.0 (compatible; HRHelpWebsite/1.0)',
  };
  // Optional shared secret. The plugin only demands it once HRHELP_CONTACT_SECRET
  // is defined in wp-config.php, so an unset binding keeps the route open.
  const wpSecret = context.env && context.env.HRHELP_WP_CONTACT_SECRET;
  if (wpSecret) headers['X-HRHelp-Secret'] = wpSecret;

  // Only the fields WordPress reads — the UTM/referrer trail is CRM-only.
  const payload = {
    name: body.name,
    email: body.email,
    company: body.company,
    phone: body.phone,
    topic: cleanTopic(body.topic),
    message: body.message,
    source: body.source,
  };

  try {
    const res = await fetch('https://admin.hrhelp.nl/wp-json/hrhelp/v1/contact', {
      method: 'POST',
      headers,
      body: JSON.stringify(payload),
    });

    // Mod Security returns an HTML block page and stores nothing.
    const contentType = res.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
      console.log('WordPress forward failed:', 'non-JSON response, status ' + res.status);
      return false;
    }

    const data = await res.json();
    if (!res.ok || !data || data.success !== true) {
      console.log('WordPress forward failed:', 'status ' + res.status);
      return false;
    }
    return true;
  } catch (error) {
    console.log('WordPress forward failed:', error.message);
    return false;
  }
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();

    // Honeypot. No human ever sees the url_confirm field, so anything in it is a
    // bot: answer exactly like a success so it learns nothing, and do no work.
    if (typeof body.url_confirm === 'string' && body.url_confirm.trim()) {
      console.log('Contact honeypot tripped');
      return Response.json({
        success: true,
        message: "Thank you! We'll get back to you within 24 hours.",
      }, { status: 200 });
    }

    // Validate required fields
    if (!body.name || !body.email) {
      return Response.json({
        success: false,
        message: 'Name and email are required.'
      }, { status: 400 });
    }

    // Two independent destinations, tried concurrently. The submission counts as
    // delivered if either one took it; only a double failure is worth telling the
    // visitor about, because then nothing anywhere holds their message.
    const [crm, wp] = await Promise.allSettled([
      sendToCrm(context, body),
      sendToWordPress(context, body),
    ]);
    const delivered = (crm.status === 'fulfilled' && crm.value) ||
                      (wp.status === 'fulfilled' && wp.value);

    if (!delivered) {
      return Response.json({
        success: false,
        message: 'We could not deliver your message. Please email us directly at info@hrhelp.nl',
      }, { status: 502 });
    }

    return Response.json({
      success: true,
      message: "Thank you! We'll get back to you within 24 hours.",
    }, { status: 200 });

  } catch (error) {
    console.error('Contact function error:', error.message);
    return Response.json({
      success: false,
      message: 'Something went wrong. Please email us at info@hrhelp.nl',
    }, { status: 500 });
  }
}

// Handle OPTIONS preflight
export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    },
  });
}
