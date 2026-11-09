// The production copy on hrhelp-website.pages.dev redirects to www.hrhelp.nl (301), so search
// engines and AI tools only ever see the real domain. Preview aliases
// (<alias>.hrhelp-website.pages.dev) and per-deploy URLs keep working for reviews.
export async function onRequest({ request, next }) {
  const url = new URL(request.url);
  if (url.hostname === 'hrhelp-website.pages.dev') {
    return Response.redirect(`https://www.hrhelp.nl${url.pathname}${url.search}`, 301);
  }
  return next();
}
