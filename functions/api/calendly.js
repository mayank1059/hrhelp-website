// Cloudflare Pages Function — relays a completed Calendly booking to the CRM.
// The browser only ever hands us two Calendly API URIs; the CRM fetches the
// booking details from Calendly itself.
//
// After the relay, still in the background (context.waitUntil), the team
// (LEAD_ALERT_TO) gets a short alert through Resend, when RESEND_API_KEY is set,
// but only when the CRM took the booking and had not seen it before (its kind
// is not skip_duplicate). A failed relay sends no email, only the log line:
// anyone can POST here, so an email per failure could send the team unlimited
// mail and use up the Resend quota the CRM's proposals and invoices share. A
// booking the relay missed is still picked up by the CRM's own Calendly pull,
// and Calendly emails the host about it itself. The browser gets 204 either way.

// Exactly api.calendly.com, then at most 200 characters of path from
// [A-Za-z0-9/_-]: no dots, spaces, newlines, query or fragment. The URIs go into
// the CRM request and the alert, so nothing else gets through.
const CALENDLY_URI = /^https:\/\/api\.calendly\.com\/[A-Za-z0-9\/_-]{1,200}$/;
const CRM_ENDPOINT = 'https://client.hrhelp.nl/api/leads/calendly';
const CRM_LEAD_URL = 'https://client.hrhelp.nl/leads/';
const RESEND_ENDPOINT = 'https://api.resend.com/emails';
// Resend sender: an address on update.hrhelp.nl, the domain verified in Resend
// (the root hrhelp.nl is not). Recipients come from the LEAD_ALERT_TO env var
// (comma-separated) so no personal addresses live in this public repo;
// info@hrhelp.nl if it is unset.
const SENDER = 'HRHelp Website Alert <website-alert@update.hrhelp.nl>';
function teamRecipients(env) {
  const raw = (env && env.LEAD_ALERT_TO) || 'info@hrhelp.nl';
  return raw.split(',').map((s) => s.trim()).filter(Boolean);
}
// The CRM asks Calendly for the booking before it answers, so it gets longer
// than the 8 seconds an email gets. Together they stay inside the 30 seconds a
// waitUntil task may run after the response.
const CRM_TIMEOUT_MS = 15000;
const EMAIL_TIMEOUT_MS = 8000;

function isCalendlyUri(value) {
  return typeof value === 'string' && CALENDLY_URI.test(value);
}

// POST with a deadline that also covers reading the answer. Never throws:
// resolves { ok, status, type, body, ms } or { ok: false, error, ms }.
async function post(url, headers, body, timeoutMs) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
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
      error: timedOut ? 'timeout after ' + timeoutMs + ' ms' : String((error && error.message) || error),
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

// Copy of the booking into the CRM at client.hrhelp.nl.
// Never throws: any failure here must stay invisible to the visitor.
async function sendToCrm(env, booking) {
  const secret = env && env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM calendly intake skipped/failed:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return { ok: false, error: 'HRHELP_LEAD_INTAKE_SECRET not set', ms: 0 };
  }
  const r = await post(CRM_ENDPOINT, {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-intake-secret': secret,
  }, JSON.stringify(booking), CRM_TIMEOUT_MS);
  if (!r.ok) logFailure('CRM calendly intake', r);
  return r;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// One email to the team (LEAD_ALERT_TO) through Resend's email API. Never throws.
async function sendEmail(env, subject, body) {
  const key = env && env.RESEND_API_KEY;
  if (!key) {
    console.log('Resend email skipped:', 'RESEND_API_KEY not set');
    return false;
  }
  const r = await post(RESEND_ENDPOINT, {
    'Authorization': 'Bearer ' + key,
    'Content-Type': 'application/json',
    // Resend refuses any request without a User-Agent (403).
    'User-Agent': 'hrhelp-website',
  }, JSON.stringify({
    from: SENDER,
    to: teamRecipients(env),
    subject,
    text: body,
    html: '<pre style="font: 14px/1.5 Arial, sans-serif; white-space: pre-wrap;">' + escapeHtml(body) + '</pre>',
  }), EMAIL_TIMEOUT_MS);
  if (!r.ok) logFailure('Resend email', r);
  return r.ok;
}

function parseJson(s) {
  try { return JSON.parse(s); } catch (e) { return null; }
}

// The relay, then the alert about it: only for a booking the CRM took and had
// not seen before. The two URIs are all this function ever knows about it.
async function relayBooking(env, booking) {
  const crm = await sendToCrm(env, booking);
  if (!crm.ok) return;
  const saved = parseJson(crm.body) || {};
  if (saved.kind === 'skip_duplicate') return;

  const intro = 'A new Calendly booking reached the CRM' +
    (saved.lead_id ? ': ' + CRM_LEAD_URL + saved.lead_id : '.') +
    (saved.kind ? '\nCRM result: ' + saved.kind : '');
  await sendEmail(env, '[HRHelp] New booking', intro + '\n\n' +
    'The website only receives the two Calendly links below; the name, email, time and any answers are in Calendly.\n\n' +
    'Calendly invitee: ' + booking.invitee_uri + '\n' +
    'Calendly event: ' + booking.event_uri + '\n');
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

  context.waitUntil(relayBooking(context.env, {
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
