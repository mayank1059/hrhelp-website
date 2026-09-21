// Cloudflare Pages Function — job applications go to the HRHelp CRM.
//
// This used to forward the whole multipart body to WordPress and nowhere else, which meant an
// application lived in the media library and the form entries of a site nobody signs into.
// The CRM at client.hrhelp.nl now has a recruitment pipeline (applicants, a journal per
// candidate, a CV shelf, a notification to the owner), so the CRM is the destination and
// WordPress is a net underneath it.
//
// TWO LEGS, IN ORDER, AND NEVER BOTH STORING
//
// The CRM is tried first. On a 2xx the application is filed, the owner has been emailed, and
// this function answers success and stops: WordPress is not called, so nothing is recorded
// twice and nobody is notified twice. Only when the CRM leg fails does the WordPress leg run,
// fire and forget, so that nothing is lost while the switch settles. The contact form
// (functions/api/contact.js) posts to both concurrently and is happy with either; this one
// deliberately does not, because a duplicated lead is a tidy-up and a duplicated application
// is a second candidate record with half a history in each.
//
// The WordPress leg keeps its own WAF tolerance: Mod Security answers an HTML challenge page
// and stores nothing, which is exactly the failure that check was written around.
//
// The response shape is unchanged, because the form in src/pages/careers/apply/[slug].astro
// reads `data.success` and `data.message` and nothing else.

const CRM_ENDPOINT = 'https://client.hrhelp.nl/api/applicants/intake';
const WP_ENDPOINT = 'https://admin.hrhelp.nl/wp-json/hrhelp/v1/apply';

// Forward the multipart body to the CRM, verbatim.
//
// The same FormData object the browser sent, handed to fetch unchanged: the file part keeps
// its filename and its content type, which is what the CRM's whitelist and its byte sniffer
// both read. Rebuilding the body field by field would be a second chance to drop the CV.
//
// Never throws: resolves true only when the CRM accepted the application.
async function sendToCrm(context, formData) {
  const secret = context.env && context.env.HRHELP_LEAD_INTAKE_SECRET;
  if (!secret) {
    console.log('CRM apply skipped/failed:', 'HRHELP_LEAD_INTAKE_SECRET not set');
    return false;
  }

  try {
    const res = await fetch(CRM_ENDPOINT, {
      method: 'POST',
      headers: {
        // No Content-Type here on purpose: fetch sets it from the FormData, including the
        // multipart boundary, and a hand written one would name a boundary that is not in
        // the body.
        'Accept': 'application/json',
        'x-intake-secret': secret,
      },
      body: formData,
    });

    // Any 2xx is success. The CRM answers 201 for a new applicant and 200 for one merged into
    // somebody already in the pipeline, and both mean the same thing here, which is that this
    // function has nothing left to do.
    if (!res.ok) {
      console.log('CRM apply skipped/failed:', 'status ' + res.status);
      return false;
    }
    return true;
  } catch (error) {
    console.log('CRM apply skipped/failed:', error.message);
    return false;
  }
}

// The fallback leg. Only runs when the CRM leg failed, so an application is never in both
// systems. Never throws.
async function sendToWordPress(formData) {
  try {
    const res = await fetch(WP_ENDPOINT, {
      method: 'POST',
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; HRHelpWebsite/1.0)',
        'Accept': 'application/json',
      },
      body: formData, // Forward multipart/form-data as-is (preserves file uploads)
    });

    // Mod Security returns an HTML block page and stores nothing.
    const contentType = res.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
      console.log('WordPress apply forward failed:', 'non-JSON response, status ' + res.status);
      return false;
    }
    if (!res.ok) {
      console.log('WordPress apply forward failed:', 'status ' + res.status);
      return false;
    }
    return true;
  } catch (error) {
    console.log('WordPress apply forward failed:', error.message);
    return false;
  }
}

export async function onRequestPost(context) {
  try {
    const formData = await context.request.formData();

    // The honeypot, answered before anything else and before any validation. No human ever
    // sees url_confirm, so anything in it is a bot: answer exactly like a success so it learns
    // nothing, and do no work. It also rides along to the CRM in the body of any request that
    // somehow gets past this, so the CRM's own guard still catches it.
    const honeypot = formData.get('url_confirm');
    if (typeof honeypot === 'string' && honeypot.trim()) {
      console.log('Apply honeypot tripped');
      return Response.json({
        success: true,
        message: "Application received! We'll review it and get back to you shortly.",
      }, { status: 200 });
    }

    // Validate required fields
    const name = formData.get('name');
    const email = formData.get('email');
    const jobTitle = formData.get('job_title');

    if (!name || !email) {
      return Response.json({
        success: false,
        message: 'Name and email are required.'
      }, { status: 400 });
    }

    if (!jobTitle) {
      return Response.json({
        success: false,
        message: 'Job title is required.'
      }, { status: 400 });
    }

    const stored = await sendToCrm(context, formData);

    if (!stored) {
      // The net. Fire and forget: the visitor should not wait on a WordPress install that is
      // being blocked by its own WAF, and there is nothing left to tell them either way,
      // because the answer below is the same whichever leg took it. waitUntil is what keeps
      // the request alive long enough for the forward to finish after the response is sent.
      const forward = sendToWordPress(formData);
      if (context.waitUntil) {
        context.waitUntil(forward);
      } else {
        await forward;
      }
    }

    return Response.json({
      success: true,
      message: "Application received! We'll review it and get back to you shortly.",
    }, { status: 200 });

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
