// /llms.txt (llmstxt.org): a plain-text map of the site for AI tools, built from the same page
// list as the HTML sitemap (src/lib/sitePages.ts), so new guides, services and posts appear in
// both. Endpoints are not pages, so it stays out of the XML sitemap.
import type { APIRoute } from 'astro';
import { getSitePages, type SitePage } from '../lib/sitePages';

const SITE = 'https://www.hrhelp.nl';

// Only facts the site itself states (homepage, about, contact, footer, terms)
const SUMMARY = 'HRhelp (HRHelp.nl) is an HR consultancy for employers with staff in the Netherlands, especially international companies. Its four solutions cover market entry, running HR for a Dutch team, HR audits and urgent cases such as dismissals. It also offers interim, fractional and other specialist HR services, has core expertise in sickness management, restructuring and leadership training, and publishes free employer guides and articles on Dutch employment law.';

const FACTS = 'HRhelp is HRHelp.nl B.V. (KvK 69913919), based at Oeverwalweg 3, 1332 CG Almere, and works across the Netherlands. It was founded in 2019 by experienced HR professionals and brings 20+ years of Dutch HR experience; its founder is Cornelis Leerlooijer. Contact: info@hrhelp.nl or +31 85 760 8188, Monday to Friday from 08:30 to 18:00 CET. Enquiries get a reply within one business day, and HR S.O.S. gives guidance on the same business day. An initial 30-minute consultation is free, and pricing is fixed and agreed upfront.';

// "- [Title](https://www.hrhelp.nl/path/): description", always on one line
const oneLine = (text: string) => text.replace(/\s+/g, ' ').trim();
const link = (p: SitePage) =>
    `- [${oneLine(p.title).replace(/[[\]]/g, '\\$&')}](${SITE}${p.path})${p.description ? `: ${oneLine(p.description)}` : ''}`;

export const GET: APIRoute = async () => {
    const site = await getSitePages();
    const { pages } = site;
    const xmlSitemap: SitePage = { path: '/sitemap-index.xml', title: 'XML sitemap', description: 'The same pages in XML, for search engines.' };

    const sections: [string, SitePage[]][] = [
        ['Services', [pages.services, ...site.services]],
        ['Solutions', [pages.solutions, ...site.solutions]],
        ['Core expertise', site.expertise],
        ['Guides', [pages.guides, ...site.guides.flatMap((g) => g.pages)]],
        ['Blog', [pages.blog, ...site.blog]],
        ['Company', [pages.about, pages.contact, pages.careers, pages.resources]],
        ['Optional', [pages.privacy, pages.terms, pages.sitemap, xmlSitemap]],
    ];

    const text = [
        '# HRhelp',
        `> ${SUMMARY}`,
        FACTS,
        ...sections.map(([title, list]) => `## ${title}\n\n${list.map(link).join('\n')}`),
    ].join('\n\n');

    return new Response(`${text}\n`, {
        headers: { 'Content-Type': 'text/plain; charset=utf-8' },
    });
};
