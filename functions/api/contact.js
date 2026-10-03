// Cloudflare Pages Function: every website lead (contact form, chatbot, guide
// downloads) goes to the HRhelp CRM at client.hrhelp.nl, and nowhere else.
// WordPress no longer receives leads: it stays as the blog CMS only.
//
//  1. The CRM is tried first, with an 8 second timeout.
//  2. CRM 2xx: the visitor gets success straight away. The CRM sends no email
//     about a new lead, so a short notification goes to the team (LEAD_ALERT_TO) through
//     Brevo after the response has been sent (context.waitUntil), when
//     BREVO_API_KEY is set.
//  3. CRM failure (error, timeout, non-2xx, or no secret): the whole lead is
//     emailed to the team (LEAD_ALERT_TO) through Brevo, and the visitor gets success only
//     if Brevo accepted that email. Otherwise 502 and the "email us" message,
//     because then nothing anywhere holds their message.

const CRM_ENDPOINT = 'https://client.hrhelp.nl/api/leads/intake';
const CRM_LEAD_URL = 'https://client.hrhelp.nl/leads/';
const BREVO_ENDPOINT = 'https://api.brevo.com/v3/smtp/email';
// Brevo sender: the address the old WordPress alerts already used, verified in
// Brevo. Recipients come from the LEAD_ALERT_TO env var (comma-separated) so no
// personal addresses live in this public repo; info@hrhelp.nl if it is unset.
const SENDER = { name: 'HRHelp Website Alert', email: 'website-alert@hrhelp.nl' };
function teamRecipients(env) {
  const raw = (env && env.LEAD_ALERT_TO) || 'info@hrhelp.nl';
  return raw.split(',').map((s) => s.trim()).filter(Boolean).map((email) => ({ email }));
}
const TIMEOUT_MS = 8000;

// The CRM's own check (EMAIL_SHAPE in its /api/leads/intake route). An address
// it would refuse gets a clear message here instead of a lost lead.
const EMAIL_SHAPE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

const SUCCESS = { success: true, message: "Thank you! We'll get back to you within one business day." };

// The contact form's placeholder option. It is disabled in the markup, so this
// is only defence in depth for cached pages that still submit it as a topic.
const TOPIC_PLACEHOLDER = 'Select a topic...';

function cleanTopic(topic) {
  if (typeof topic !== 'string') return '';
  const trimmed = topic.trim();
  return trimmed === TOPIC_PLACEHOLDER ? '' : trimmed;
}

function text(value, max) {
  return typeof value === 'string' ? value.trim().slice(0, max) : '';
}

// Host of a referrer the browser reported, or '' (the forms send a hostname,
// older cached pages a full URL). Our own host is not a referrer.
function refHost(value) {
  let host = text(value, 300).toLowerCase();
  if (host.includes('/')) {
    try { host = new URL(host).hostname; } catch (e) { host = ''; }
  }
  host = host.replace(/^www\./, '');
  return /(^|\.)hrhelp\.nl$/.test(host) ? '' : host;
}

// Where the lead came from, as one readable label for the CRM card and the
// notification email. Input: the first-touch attribution the site stores on
// landing (utm_*, gclid/gbraid/wbraid, fbclid, referrer host). Tested in isolation.
export function leadSource(a) {
  const src = text(a.utm_source, 100).toLowerCase();
  const med = text(a.utm_medium, 100).toLowerCase();
  const ref = refHost(a.referrer);
  const paid = /^(cpc|ppc|paid|paid[-_ ]?(search|social)|cpm|display)$/.test(med);
  const isMeta = /facebook|instagram|meta|^fb$|^ig$/.test(src);

  if (text(a.gclid, 200) || text(a.gbraid, 200) || text(a.wbraid, 200)) return 'Google Ads';
  if (paid && src.includes('google')) return 'Google Ads';
  if (paid && isMeta) return 'Meta Ads';
  if (text(a.fbclid, 200) && !src) return 'Meta Ads';
  if (paid && /bing|microsoft/.test(src)) return 'Microsoft Ads';
  if (paid && src.includes('linkedin')) return 'LinkedIn Ads';
  if (med === 'email' || med === 'newsletter') return 'Email';
  if (paid) return 'Paid: ' + src;
  if (src.includes('linkedin') || /(^|\.)linkedin\.com$|^lnkd\.in$/.test(ref)) return 'LinkedIn';
  if (src) return 'Campaign: ' + src;
  if (/(^|\.)google\.[a-z.]+$|googlequicksearchbox/.test(ref)) return 'Google organic';
  if (/(^|\.)bing\.com$/.test(ref)) return 'Bing organic';
  if (ref) return 'Referral: ' + ref;
  return 'Direct';
}

// The attribution lines at the top of the message: the CRM's only free-text
// field, and the first thing the notification email shows.
function sourceBlock(body, label) {
  const lines = ['Lead source: ' + label];
  const campaign = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']
    .map((k) => (text(body[k], 150) ? k + '=' + text(body[k], 150) : ''))
    .filter(Boolean);
  if (campaign.length) lines.push('Campaign: ' + campaign.join(', '));
  const clicks = ['gclid', 'gbraid', 'wbraid', 'fbclid']
    .map((k) => (text(body[k], 200) ? k + '=' + text(body[k], 200) : ''))
    .filter(Boolean);
  if (clicks.length) lines.push('Click ID: ' + clicks.join(', '));
  const ref = refHost(body.referrer);
  if (ref) lines.push('Referrer: ' + ref);
  if (text(body.landing_page, 200)) lines.push('Landing page: ' + text(body.landing_page, 200));
  return lines.join('\n');
}

// The guide download forms (homepage, footer) send a source label starting with
// "Whitepaper Download". They also send marketing_consent: true only when the
// visitor ticked the optional "HR updates" box.
function isGuideDownload(body) {
  return /^whitepaper download/i.test(text(body.source, 60));
}

// One mapping for every form, so the CRM and the email get the same thing. The
// contact form and the chatbot send the same structured answers (who, needs[],
// employees, timeline, preferred_contact, page); those become labelled lines,
// and the chosen help topics become the topic when none is given. A guide
// download gets a "Marketing consent: yes/no" line, because the CRM has no field
// for it. Every submission gets the lead-source block on top and a channel label
// "<form> · <lead source>" (the CRM shows it on the lead card).
function prepare(body) {
  const needs = Array.isArray(body.needs)
    ? body.needs.map((n) => text(n, 80)).filter(Boolean).slice(0, 10)
    : [];
  const rows = [
    ['Who', text(body.who, 120)],
    ['Help needed', needs.join('; ')],
    ['Employees in the Netherlands', text(body.employees, 40)],
    ['Timeline', text(body.timeline, 40)],
    ['Preferred contact', text(body.preferred_contact, 40)],
    ['Page', text(body.page, 200)],
    ['Marketing consent', isGuideDownload(body) ? (body.marketing_consent === true ? 'yes' : 'no') : ''],
  ].filter((row) => row[1]);

  // Same cap as the contact form's textarea (maxlength 5000).
  const note = text(body.message, 5000);
  const details = rows.map((row) => row[0] + ': ' + row[1]).join('\n');
  const enquiry = rows.length
    ? (note ? details + '\n\nMessage:\n' + note : details)
    : note;
  const label = leadSource(body);
  const form = text(body.source, 60);
  return {
    name: text(body.name, 120),
    email: text(body.email, 200),
    company: text(body.company, 160),
    phone: text(body.phone, 40),
    // The guide downloads send no topic but do send a source label
    // ("Whitepaper Download"); without it a guide download would be
    // indistinguishable from a contact lead in the CRM.
    topic: cleanTopic(body.topic) || needs.join(', ').slice(0, 120) || form,
    message: sourceBlock(body, label) + (enquiry ? '\n\n' + enquiry : ''),
    channel: (form ? form + ' · ' + label : label).slice(0, 80),
  };
}

// POST with a deadline that also covers reading the answer. Never throws:
// resolves { ok, status, type, body, ms } or { ok: false, error, ms }.
async function post(url, headers, body) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), TIMEOUT_MS);
  const started = Date.now();
  try {
    const res = await fetch(url, { method: 'POST', headers, body, signal: controller.signal });
    const answer = await res.text();
    return {
      ok: res.ok,
      status: res.status,
      type: res.headers.get('content-type') || '',
      body: answer,
      ms: Date.now() - started,
    };
  } catch (error) {
    const timedOut = error && error.name === 'AbortError';
    return {
      ok: false,
      error: timedOut ? 'timeout after ' + TIMEOUT_MS + ' ms' : String((error && error.message) || error),
      ms: Date.now() - started,
    };
  } finally {
    clearTimeout(timer);
  }
}

// Status, content type, latency and the start of the body, for the Pages log.
function logFailure(what, r) {
  if (r.error) {
    console.log(what + ' failed:', r.error + ' after ' + r.ms + ' ms');
    return;
  }
  console.log(
    what + ' failed:',
    'status ' + r.status,
    '| content-type ' + (r.type || 'none'),
    '| ' + r.ms + ' ms',
    '| body ' + JSON.stringify(r.body.slice(0, 200)),
  );
}

// The lead into the CRM. The CRM uses the same url_confirm name for its own
// honeypot; nothing reaches here with it filled, because onRequestPost answers
// bots first.
async function sendToCrm(env, lead) {
  const secret = env && env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM intake skipped:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return { ok: false, error: 'HRHELP_LEAD_INTAKE_SECRET not set', ms: 0 };
  }
  const r = await post(CRM_ENDPOINT, {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-intake-secret': secret,
  }, JSON.stringify({
    name: lead.name,
    email: lead.email,
    company: lead.company,
    phone: lead.phone,
    topic: lead.topic,
    message: lead.message,
    // "<form> · <lead source>", e.g. "Website chatbot · Google Ads"; the CRM
    // shows it as a pill on the lead card (capped at 80 there).
    channel: lead.channel,
  }));
  if (!r.ok) logFailure('CRM intake', r);
  return r;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// One email to the team (LEAD_ALERT_TO) through Brevo's transactional API. Never throws:
// resolves true only when Brevo accepted it (2xx; it answers 201 with a messageId).
async function sendEmail(env, subject, body, replyTo) {
  const key = env && env.BREVO_API_KEY;
  if (!key) {
    console.log('Brevo email skipped:', 'BREVO_API_KEY not set');
    return false;
  }
  const payload = {
    sender: SENDER,
    to: teamRecipients(env),
    subject,
    textContent: body,
    htmlContent: '<pre style="font: 14px/1.5 Arial, sans-serif; white-space: pre-wrap;">' + escapeHtml(body) + '</pre>',
  };
  if (replyTo) payload.replyTo = replyTo;
  const r = await post(BREVO_ENDPOINT, {
    'api-key': key,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }, JSON.stringify(payload));
  if (!r.ok) logFailure('Brevo email', r);
  return r.ok;
}

// Every field of the lead, under a one-line explanation. The message already
// starts with the lead-source block.
function leadEmail(lead, intro) {
  const rows = [
    ['Name', lead.name],
    ['Email', lead.email],
    ['Company', lead.company],
    ['Phone', lead.phone],
    ['Topic', lead.topic],
    ['Form', lead.channel],
  ].filter((row) => row[1]).map((row) => row[0] + ': ' + row[1]);
  return intro + '\n\n' + rows.join('\n') + '\n\n' + lead.message + '\n';
}

// Replies go straight to the visitor. Only for a plain ASCII address, so an
// unusual one can never make Brevo refuse the email itself.
function replyToFor(lead) {
  return /^[\x21-\x7e]+$/.test(lead.email)
    ? { email: lead.email, name: lead.name.slice(0, 70) }
    : undefined;
}

function parseJson(s) {
  try { return JSON.parse(s); } catch (e) { return null; }
}

export async function onRequestPost(context) {
  try {
    const body = await context.request.json();

    // Honeypot. No human ever sees the url_confirm field, so anything in it is a
    // bot: answer exactly like a success so it learns nothing, and do no work.
    if (typeof body.url_confirm === 'string' && body.url_confirm.trim()) {
      console.log('Contact honeypot tripped');
      return Response.json(SUCCESS, { status: 200 });
    }

    if (!text(body.name, 120) || !text(body.email, 200)) {
      return Response.json({ success: false, message: 'Name and email are required.' }, { status: 400 });
    }
    if (!EMAIL_SHAPE.test(text(body.email, 200))) {
      return Response.json({ success: false, message: 'Please enter a valid email address.' }, { status: 400 });
    }

    const lead = prepare(body);
    // A name on one line, for the subject.
    const who = lead.name.replace(/\s+/g, ' ');
    const crm = await sendToCrm(context.env, lead);

    if (crm.ok) {
      if (context.env && context.env.BREVO_API_KEY) {
        const saved = parseJson(crm.body) || {};
        const link = saved.lead_id ? CRM_LEAD_URL + saved.lead_id : '';
        const intro = (saved.merged
          ? 'A new message from a lead already in the CRM'
          : 'A new lead is in the CRM') + (link ? ': ' + link : '.');
        const subject = '[HRHelp] ' + (saved.merged ? 'New message: ' : 'New lead: ') + who;
        const notify = sendEmail(context.env, subject, leadEmail(lead, intro), replyToFor(lead));
        if (context.waitUntil) context.waitUntil(notify);
      }
      return Response.json(SUCCESS, { status: 200 });
    }

    // The CRM did not take it: email the whole lead instead, and only tell the
    // visitor it arrived if that email was accepted.
    const reason = crm.error || 'the CRM answered ' + crm.status;
    const intro = 'The website could not save this lead in the CRM (' + reason + ').\n' +
      'Please add it to the CRM by hand and reply to the visitor.';
    const emailed = await sendEmail(
      context.env,
      '[HRHelp] Lead not saved in CRM: ' + who,
      leadEmail(lead, intro),
      replyToFor(lead),
    );
    if (emailed) return Response.json(SUCCESS, { status: 200 });

    return Response.json({
      success: false,
      message: 'We could not deliver your message. Please email us directly at info@hrhelp.nl',
    }, { status: 502 });

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
