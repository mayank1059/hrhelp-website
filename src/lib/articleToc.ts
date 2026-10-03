// Table of contents for long-form pages (blog posts, guides): gives every <h2>
// in an HTML string an id (keeps an existing one) and returns the list for the
// "On this page" navigation. Heading text and levels are left untouched.
export interface TocItem { id: string; html: string }

const slugify = (s: string) => {
  const slug = s.toLowerCase()
    .replace(/&#0?39;|&#8217;|&rsquo;|&apos;|['\u2019]/g, '') // don't -> dont
    .replace(/&[#a-z0-9]+;/g, ' ')
    .normalize('NFKD').replace(/[\u0300-\u036f]/g, '')
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  // Max ~60 characters, cut at a word boundary
  const short = slug.length > 60 ? slug.slice(0, 61).replace(/-[^-]*$/, '') : slug;
  return short || 'section';
};

export function addHeadingIds(html: string): { html: string; toc: TocItem[] } {
  const toc: TocItem[] = [];
  const used = new Set<string>();
  const out = html.replace(/<h2(\s[^>]*)?>([\s\S]*?)<\/h2>/gi, (match, attrs = '', inner) => {
    // Link text: the heading's text with tags removed (entities stay encoded)
    const text = inner.replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
    if (!text) return match;
    const existing = attrs.match(/\sid=["']([^"']+)["']/i);
    let id = existing ? existing[1] : slugify(text);
    if (!existing) {
      let n = 2;
      const base = id;
      while (used.has(id)) id = `${base}-${n++}`;
    }
    used.add(id);
    toc.push({ id, html: text });
    return existing ? match : `<h2${attrs} id="${id}">${inner}</h2>`;
  });
  return { html: out, toc };
}
