// Cloudflare Pages Function — relays a completed Calendly booking to the CRM.
// The browser only ever hands us two Calendly API URIs; the CRM fetches the
// booking details from Calendly itself.

const CALENDLY_API_PREFIX = 'https://api.calendly.com/';

function isCalendlyUri(value) {
  return typeof value === 'string' && value.startsWith(CALENDLY_API_PREFIX);
}

// Fire-and-forget copy of the booking into the CRM at client.hrhelp.nl.
// Never throws: any failure here must stay invisible to the visitor.
async function sendToCrm(secret, booking) {
  try {
    const res = await fetch('https://client.hrhelp.nl/api/leads/calendly', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'x-intake-secret': secret,
      },
      body: JSON.stringify(booking),
    });
    if (!res.ok) {
      console.log('CRM calendly intake skipped/failed:', 'status ' + res.status);
    }
  } catch (error) {
    console.log('CRM calendly intake skipped/failed:', error.message);
  }
}

export async function onRequestPost(context) {
  let body;
  try {
    body = await context.request.json();
  } catch {
    return Response.json({ ok: false }, { status: 400 });
  }

  // Only Calendly's own API URIs get through — this is the SSRF/spam guard.
  if (!body || !isCalendlyUri(body.invitee_uri) || !isCalendlyUri(body.event_uri)) {
    return Response.json({ ok: false }, { status: 400 });
  }

  const secret = context.env && context.env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM calendly intake skipped/failed:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return new Response(null, { status: 204 });
  }

  context.waitUntil(sendToCrm(secret, {
    invitee_uri: body.invitee_uri,
    event_uri: body.event_uri,
  }));

  return new Response(null, { status: 204 });
}

// A stray browser hit should not 500.
export async function onRequestGet() {
  return Response.json({ ok: false }, { status: 405 });
}

export async function onRequestOptions() {
  return Response.json({ ok: false }, { status: 405 });
}
