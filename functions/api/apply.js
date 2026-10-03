// Cloudflare Pages Function: job applications go to the HRhelp CRM at
// client.hrhelp.nl, and nowhere else. WordPress no longer receives them.
//
// The CRM files the applicant, stores the CV and notifies the owner itself, so
// on a CRM 2xx this function answers success and stops.
//
// When the CRM fails (error, timeout, non-2xx, or no secret), the application is
// emailed to the team (LEAD_ALERT_TO) through Brevo instead, with the CV attached when
// Brevo can take it (PDF or Word, at most 4 MB). The candidate hears
// "Application received" only when the CRM or that email accepted it:
//  - email accepted with the CV (or no CV was uploaded): success;
//  - email accepted without the CV (too big, wrong type, or refused by Brevo):
//    an error asking the candidate to email the CV, because nothing holds it;
//  - no email either: 502 and the "email your application" message.
//
// The response shape is unchanged: the form in src/pages/careers/apply/[slug].astro
// reads `data.success` and `data.message` and nothing else.

const CRM_ENDPOINT = 'https://client.hrhelp.nl/api/applicants/intake';
const BREVO_ENDPOINT = 'https://api.brevo.com/v3/smtp/email';
// Brevo sender: the address the old WordPress alerts already used, verified in
// Brevo. Recipients come from the LEAD_ALERT_TO env var (comma-separated) so no
// personal addresses live in this public repo; info@hrhelp.nl if it is unset.
const SENDER = { name: 'HRHelp Website Alert', email: 'website-alert@hrhelp.nl' };
function teamRecipients(env) {
  const raw = (env && env.LEAD_ALERT_TO) || 'info@hrhelp.nl';
  return raw.split(',').map((s) => s.trim()).filter(Boolean).map((email) => ({ email }));
}
// The CRM leg carries the CV, so it gets longer than the 8 seconds an email gets.
const CRM_TIMEOUT_MS = 15000;
const EMAIL_TIMEOUT_MS = 8000;
// Brevo's limit for one attachment, and the types the form offers.
const MAX_ATTACHMENT_BYTES = 4 * 1024 * 1024;
const CV_TYPES = /\.(pdf|doc|docx)$/i;
// The CRM's own check (APPLICANT_EMAIL_SHAPE in its applicant intake).
const EMAIL_SHAPE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

const RECEIVED = { success: true, message: "Application received! We'll review it and get back to you shortly." };
const NOT_SENT = {
  success: false,
  message: 'We could not submit your application. Please email it to info@hrhelp.nl',
};
const CV_NOT_SENT = {
  success: false,
  message: 'We have your details, but your CV could not be uploaded. Please email your CV to info@hrhelp.nl and mention the role you applied for.',
};

function field(formData, key, max) {
  const value = formData.get(key);
  return typeof value === 'string' ? value.trim().slice(0, max) : '';
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

// The multipart body to the CRM, verbatim: the same FormData the browser sent,
// so the CV keeps its filename and content type, which the CRM's whitelist and
// byte sniffer both read. No Content-Type header on purpose: fetch sets it from
// the FormData, including the boundary. Any 2xx is success (201 for a new
// applicant, 200 for one merged into an open record).
async function sendToCrm(env, formData) {
  const secret = env && env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM apply skipped:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return { ok: false, error: 'HRHELP_LEAD_INTAKE_SECRET not set', ms: 0 };
  }
  const r = await post(CRM_ENDPOINT, {
    'Accept': 'application/json',
    'x-intake-secret': secret,
  }, formData, CRM_TIMEOUT_MS);
  if (!r.ok) logFailure('CRM apply', r);
  return r;
}

function escapeHtml(s) {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// One email to the team (LEAD_ALERT_TO) through Brevo's transactional API. Never throws.
async function sendEmail(env, subject, body, replyTo, attachment) {
  const payload = {
    sender: SENDER,
    to: teamRecipients(env),
    subject,
    textContent: body,
    htmlContent: '<pre style="font: 14px/1.5 Arial, sans-serif; white-space: pre-wrap;">' + escapeHtml(body) + '</pre>',
  };
  if (replyTo) payload.replyTo = replyTo;
  if (attachment) payload.attachment = [attachment];
  const r = await post(BREVO_ENDPOINT, {
    'api-key': env.BREVO_API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  }, JSON.stringify(payload), EMAIL_TIMEOUT_MS);
  if (!r.ok) logFailure('Brevo email', r);
  return r;
}

// Base64 in slices, because String.fromCharCode cannot take megabytes at once.
function toBase64(buffer) {
  const bytes = new Uint8Array(buffer);
  let binary = '';
  for (let i = 0; i < bytes.length; i += 0x8000) {
    binary += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  }
  return btoa(binary);
}

function megabytes(bytes) {
  return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
}

// The application by email, when the CRM did not take it.
async function emailApplication(env, formData, reason) {
  const name = field(formData, 'name', 160);
  const email = field(formData, 'email', 200);
  const job = field(formData, 'job_title', 160);
  const resume = formData.get('resume');
  const cv = resume && typeof resume === 'object' && resume.size > 0 ? resume : null;

  let attachment = null;
  let cvLine = 'none uploaded';
  if (cv && cv.size > MAX_ATTACHMENT_BYTES) {
    cvLine = 'NOT attached: ' + cv.name + ' is ' + megabytes(cv.size) + ', over the 4 MB email limit. The candidate was asked to email it.';
  } else if (cv && !CV_TYPES.test(cv.name)) {
    cvLine = 'NOT attached: ' + cv.name + ' is not a PDF or Word file. The candidate was asked to email it.';
  } else if (cv) {
    attachment = {
      name: cv.name.replace(/[^\w.() -]+/g, '_').slice(-100),
      content: toBase64(await cv.arrayBuffer()),
    };
    cvLine = 'attached (' + cv.name + ', ' + megabytes(cv.size) + ')';
  }

  const message = (line) => [
    'The website could not save this application in the CRM (' + reason + ').',
    'Please add it to the CRM by hand.',
    '',
    'Vacancy: ' + job + (field(formData, 'job_slug', 160) ? ' (' + field(formData, 'job_slug', 160) + ')' : ''),
    'Name: ' + name,
    'Email: ' + email,
    'Phone: ' + (field(formData, 'phone', 40) || '-'),
    'LinkedIn: ' + (field(formData, 'linkedin', 300) || '-'),
    'CV: ' + line,
    '',
    'Cover letter:',
    field(formData, 'cover_letter', 8000) || '-',
    '',
  ].join('\n');
  const subject = '[HRHelp] Application not saved in CRM: ' + name.replace(/\s+/g, ' ');
  const replyTo = /^[\x21-\x7e]+$/.test(email) ? { email, name: name.slice(0, 70) } : undefined;

  let r = await sendEmail(env, subject, message(cvLine), replyTo, attachment);
  // Brevo refused the email that carried the CV (a 4xx is about the content, for
  // example a file it will not take): send the details alone.
  if (!r.ok && attachment && r.status >= 400 && r.status < 500) {
    attachment = null;
    r = await sendEmail(env, subject, message('NOT attached: Brevo refused the email with ' + cv.name + '. The candidate was asked to email it.'), replyTo, null);
  }
  return { sent: r.ok, cvMissing: Boolean(cv) && !attachment };
}

export async function onRequestPost(context) {
  try {
    const formData = await context.request.formData();

    // The honeypot, answered before anything else and before any validation. No
    // human ever sees url_confirm, so anything in it is a bot: answer exactly like
    // a success so it learns nothing, and do no work.
    const honeypot = formData.get('url_confirm');
    if (typeof honeypot === 'string' && honeypot.trim()) {
      console.log('Apply honeypot tripped');
      return Response.json(RECEIVED, { status: 200 });
    }

    if (!field(formData, 'name', 160) || !field(formData, 'email', 200)) {
      return Response.json({ success: false, message: 'Name and email are required.' }, { status: 400 });
    }
    if (!EMAIL_SHAPE.test(field(formData, 'email', 200))) {
      return Response.json({ success: false, message: 'Please enter a valid email address.' }, { status: 400 });
    }
    if (!field(formData, 'job_title', 160)) {
      return Response.json({ success: false, message: 'Job title is required.' }, { status: 400 });
    }

    const crm = await sendToCrm(context.env, formData);
    if (crm.ok) return Response.json(RECEIVED, { status: 200 });

    if (!(context.env && context.env.BREVO_API_KEY)) {
      console.log('Brevo email skipped:', 'BREVO_API_KEY not set');
      return Response.json(NOT_SENT, { status: 502 });
    }
    const { sent, cvMissing } = await emailApplication(context.env, formData, crm.error || 'the CRM answered ' + crm.status);
    if (!sent) return Response.json(NOT_SENT, { status: 502 });
    if (cvMissing) return Response.json(CV_NOT_SENT, { status: 502 });
    return Response.json(RECEIVED, { status: 200 });

  } catch (error) {
    console.error('Apply function error:', error.message);
    return Response.json({
      success: false,
      message: 'Something went wrong. Please email your application to info@hrhelp.nl',
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
