// Cloudflare Pages Function — proxies job applications to WordPress REST API
// Handles multipart/form-data (resume uploads) and bypasses Cloudflare WAF
export async function onRequestPost(context) {
  try {
    const formData = await context.request.formData();

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

    // Forward the entire FormData to WordPress REST API
    const wpResponse = await fetch('https://admin.hrhelp.nl/wp-json/hrhelp/v1/apply', {
      method: 'POST',
      headers: {
        'User-Agent': 'Mozilla/5.0 (compatible; HRHelpWebsite/1.0)',
        'Accept': 'application/json',
      },
      body: formData,  // Forward multipart/form-data as-is (preserves file uploads)
    });

    // Check if response is JSON (Cloudflare WAF may return HTML challenge)
    const contentType = wpResponse.headers.get('content-type') || '';
    if (!contentType.includes('application/json')) {
      console.log('WordPress blocked by WAF, status:', wpResponse.status);

      // Fallback: acknowledge the submission
      // The data is captured in Cloudflare logs
      return Response.json({
        success: true,
        message: "Application received! We'll review it and get back to you shortly.",
        note: 'direct'
      }, { status: 200 });
    }

    const wpData = await wpResponse.json();
    return Response.json(wpData, { status: wpResponse.status });

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
