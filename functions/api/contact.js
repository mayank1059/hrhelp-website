// Cloudflare Pages Function — proxies form submissions to WordPress REST API
// This bypasses CORS and Mod Security issues on the hosting provider
export async function onRequestPost(context) {
  try {
    const body = await context.request.json();

    // Validate required fields
    if (!body.name || !body.email) {
      return new Response(JSON.stringify({
        success: false,
        message: 'Name and email are required.'
      }), { status: 400, headers: { 'Content-Type': 'application/json' } });
    }

    // Forward to WordPress REST API (server-to-server, no CORS/ModSec issues)
    const wpResponse = await fetch('https://admin.hrhelp.nl/wp-json/hrhelp/v1/contact', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });

    const wpData = await wpResponse.json();

    return new Response(JSON.stringify(wpData), {
      status: wpResponse.status,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (error) {
    return new Response(JSON.stringify({
      success: false,
      message: 'Server error. Please try again later.',
    }), { status: 500, headers: { 'Content-Type': 'application/json' } });
  }
}

// Handle OPTIONS preflight (shouldn't be needed for same-origin, but just in case)
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
