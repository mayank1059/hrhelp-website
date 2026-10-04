// The site's pages with their titles, shared by /llms.txt (src/pages/llms.txt.ts) and the
// HTML sitemap (src/pages/sitemap.astro). The lists come from the same data the routes are
// built from (staging-gated services and guides, WordPress), so both stay current on their own.
// Titles are the page titles without " | HRHelp.nl", descriptions the meta descriptions (set
// where /llms.txt shows one). The fixed pages, the solution descriptions and the industry
// names repeat what those pages' own .astro files set: change both together.
import { decodeHTMLEntities, getBlogPosts, getCaseStudies, getExpertiseItems, getJobOpenings } from './wordpress';
import { getExpertiseContent } from './expertiseContent';
import { solutions, solutionBySlug } from '../data/solutions.js';
import { serviceLinks } from '../data/pseo/service-groups.js';
import { settlersData, teamsData, sosData } from '../data/pseo/guides.js';

export interface SitePage {
  /** Site-relative, with the trailing slash the site links with */
  path: string;
  title: string;
  description?: string;
}

const page = (path: string, title: string, description?: string): SitePage => ({ path, title, description });

// Meta descriptions of src/pages/solutions/[slug].astro (each solution's hero text)
const SOLUTION_DESCRIPTIONS: Record<string, string> = {
  'hr-settlers': 'Complete HR setup for companies establishing their first Netherlands presence. From entity registration to your first employee, we handle everything.',
  'hr-teams': 'A dedicated HR manager for your Netherlands operation. Full lifecycle HR support without the overhead of an in-house department.',
  'hr-reset': 'A thorough HR audit and transformation for companies with compliance gaps, outdated contracts, or legacy processes that need modernization.',
  'hr-sos': 'Rapid-response HR support for urgent situations. Same-day guidance for dismissals, workplace conflicts, and compliance emergencies.',
};

// Pages of src/pages/industries/[slug].astro, in the order of /industries/
const INDUSTRIES: [slug: string, name: string][] = [
  ['technology', 'Technology & Startups'],
  ['life-sciences', 'Life Sciences & Pharma'],
  ['finance', 'Finance & Fintech'],
  ['professional-services', 'Professional Services'],
  ['logistics', 'Logistics & Supply Chain'],
  ['ngo', 'NGO & Non-Profit'],
  ['manufacturing', 'Greenfield & Manufacturing'],
  ['industrial', 'Production & Industrial'],
];

// Guide verticals; each id is also the slug of the matching solution
const GUIDE_VERTICALS: [id: string, guides: any[]][] = [
  ['hr-settlers', settlersData],
  ['hr-teams', teamsData],
  ['hr-sos', sosData],
];

export async function getSitePages() {
  const [posts, expertise, caseStudies, jobs] = await Promise.all([
    getBlogPosts(), getExpertiseItems(), getCaseStudies(), getJobOpenings(),
  ]);
  const guideCount = GUIDE_VERTICALS.reduce((n, [, guides]) => n + guides.length, 0);

  return {
    // Fixed pages: the title and meta description their own .astro file sets
    pages: {
      home: page('/', 'Home', 'Expert HR consulting for international companies in the Netherlands. Employment law, payroll, compliance, talent acquisition, all handled by Dutch HR experts.'),
      about: page('/about/', 'About Us', 'Founded in 2019 to humanize Dutch HR for international companies. Learn about our founder Cornelis Leerlooijer and our network of specialists.'),
      partners: page('/about/partners/', 'Partners', "Discover the specialized partners that make up HRHelp.nl's network organization, each an expert in their HR field."),
      contact: page('/contact/', 'Contact Us', 'Get in touch with HRHelp.nl for specialized HR support for international companies in the Netherlands. Free consultation, Almere office.'),
      careers: page('/careers/', 'Careers', 'Join HRHelp.nl as a specialized HR consultant or network partner. Shape the future of Dutch HR for international companies.'),
      resources: page('/resources/', 'HR Resources for Employers in the Netherlands', `Free resources for international employers in the Netherlands: ${guideCount} HR guides, articles on Dutch employment law, case studies, FAQs and a 2026 HR rules guide.`),
      faq: page('/resources/faq/', 'FAQ', 'Common questions about HRHelp.nl services, Dutch HR law, the 30% ruling, and our network organization model.'),
      caseStudies: page('/resources/case-studies/', 'Case Studies', "Real challenges, measurable outcomes: case studies from HRHelp.nl's client engagements."),
      industries: page('/industries/', 'Industries', 'Specialized HR consulting across key sectors of the Dutch economy: technology, healthcare, finance, manufacturing, and more.'),
      services: page('/services/', 'HR Services Netherlands: Interim, Fractional & Compliance', 'Specialist HR services for international companies in the Netherlands. Interim and fractional HR, embedded HR roles, Dutch entity compliance and labour law advice. Fixed pricing.'),
      solutions: page('/solutions/', 'Solutions', 'HR solutions for every stage of doing business in the Netherlands. From market entry to full HR outsourcing.'),
      guides: page('/guides/', 'HR Guides & Resources', 'Guides for international companies dealing with Dutch employment law, HR compliance, and business setup in the Netherlands.'),
      blog: page('/blog/', 'Blog & Insights', 'Expert articles, guides, and insights on Dutch employment law, HR strategy, and managing international teams in the Netherlands.'),
      privacy: page('/privacy/', 'Privacy Policy', 'Privacy Policy and GDPR compliance information for HRHelp.nl B.V., your trusted Dutch HR partner.'),
      terms: page('/terms/', 'General Terms and Conditions', 'General Terms and Conditions for HRHelp.nl: Dutch HR consultancy services for international companies.'),
      sitemap: page('/sitemap/', 'Sitemap', 'Every page on HRHelp.nl in one list: HR services and solutions, core expertise, industries, employer guides, blog articles, resources and company information.'),
    },
    // Every visible service, in the order of the footer and the services index
    services: serviceLinks.map((s: any) => page(`/services/${s.slug}/`, s.title || s.name, s.metaDescription || s.subtitle || s.hero)),
    solutions: solutions.map((s) => page(`/solutions/${s.slug}/`, s.name, SOLUTION_DESCRIPTIONS[s.slug])),
    // Title and description as src/pages/expertise/[slug].astro sets them
    expertise: expertise.map((e) => {
      const seo = getExpertiseContent(e.slug)?.seo;
      return page(`/expertise/${e.slug}/`, decodeHTMLEntities(seo?.title || e.title), decodeHTMLEntities(seo?.description || e.intro.slice(0, 160)));
    }),
    industries: INDUSTRIES.map(([slug, name]) => page(`/industries/${slug}/`, `${name} HR Consulting`)),
    // Per vertical: its overview page (only built when it has guides) and its guides
    guides: GUIDE_VERTICALS.filter(([, guides]) => guides.length > 0).map(([id, guides]) => ({
      hub: page(`/guides/${id}/`, `${solutionBySlug[id].name} Guides`),
      pages: guides.map((g) => page(`/guides/${g.slug}/`, g.title, g.subtitle)),
    })),
    // Newest first
    blog: posts
      .map((p) => ({ p, ts: Date.parse(p.datePublished || p.date) || 0 }))
      .sort((a, b) => b.ts - a.ts)
      .map(({ p }) => page(`/blog/${p.slug}/`, p.title, p.excerpt)),
    caseStudies: caseStudies.map((cs) => page(`/resources/case-studies/${cs.slug}/`, decodeHTMLEntities(cs.title))),
    jobs: jobs.map((j) => page(`/careers/apply/${j.slug}/`, j.title)),
  };
}
