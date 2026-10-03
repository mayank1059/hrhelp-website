/**
 * WordPress Headless CMS API Client
 * Fetches resources content (case studies, expertise, FAQ) from WordPress REST API.
 * If WordPress is unreachable or answers with an error, the build fails, so CI keeps the
 * last good deploy instead of publishing fallback content. WP_ALLOW_FALLBACK=1 (local
 * development) builds with the hardcoded fallback data instead.
 */

import {
    fallbackCaseStudies,
    fallbackExpertise,
    fallbackFAQGroups,
    fallbackBlogPosts,
    fallbackJobOpenings,
} from './fallback-data';
import { solutions } from '../data/solutions.js';
import { settlersData, teamsData, sosData } from '../data/pseo/guides.js';
import { servicesData } from '../data/pseo/services.js';

// ---------- CONFIG ----------
const WP_URL = import.meta.env.PUBLIC_WP_URL || '';
const ALLOW_FALLBACK = process.env.WP_ALLOW_FALLBACK === '1' || import.meta.env.WP_ALLOW_FALLBACK === '1';

// ---------- TYPE INTERFACES ----------

export interface FloatCard {
    icon: string;
    label: string;
    value: string;
}

export interface FloatCards {
    tl: FloatCard;
    br: FloatCard;
}

export interface Stat {
    value: string;
    label: string;
}

export interface CaseStudy {
    slug: string;
    tag: string;
    title: string;
    intro: string;
    icon: string;
    color: string;
    image: string;
    illustration: string;
    items: string[];
    outcome: string;
    stats: Stat[];
    floatCards: FloatCards;
    context: string;
}

export interface IncludedItem {
    title: string;
    desc: string;
}

export interface Expertise {
    slug: string;
    title: string;
    subtitle: string;
    tagline: string;
    icon: string;
    image: string;
    illustration: string;
    intro: string;
    floatCards: FloatCards;
    premiseHeading: string;
    premiseBody: string[];
    included: IncludedItem[];
    result: string;
    stats: Stat[];
}

export interface FAQItem {
    q: string;
    a: string;
}

export interface FAQGroup {
    category: string;
    items: FAQItem[];
}

export interface BlogPost {
    slug: string;
    title: string;
    excerpt: string;
    content: string;
    category: string[];
    image: string;
    date: string;
    /** Last-modified date, same format as date; empty when WP has none */
    modified?: string;
    /** Publish and last-modified dates in ISO 8601 (for structured data); empty when WP has none */
    datePublished?: string;
    dateModified?: string;
    readTime: string;
    author: string;
    /** Only the categories actually set on the post (no 'Article' default); empty when it has none. */
    tags?: string[];
}

export interface JobOpening {
    slug: string;
    title: string;
    type: string;
    location: string;
    description: string;
    /** WordPress publish date in ISO 8601, for JobPosting.datePosted */
    datePosted?: string;
    /** Where the job is, for JobPosting.jobLocation (see jobPlaces); empty when nothing is named */
    places?: JobPlace[];
    /** The location field says the job is fully remote, for JobPosting TELECOMMUTE */
    remote?: boolean;
}

export interface JobPlace {
    locality?: string;
    region?: string;
    country: string;
}

// ---------- HELPER ----------

const NAMED_ENTITIES: Record<string, string> = {
    amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ', shy: '',
    hellip: '…', ndash: '–', mdash: '—', lsquo: "'", rsquo: "'", ldquo: '"', rdquo: '"',
    sbquo: '‚', bdquo: '„', laquo: '«', raquo: '»', bull: '•', middot: '·',
    copy: '©', reg: '®', trade: '™', euro: '€', deg: '°', times: '×',
    eacute: 'é', egrave: 'è', euml: 'ë', iuml: 'ï', ouml: 'ö', uuml: 'ü', auml: 'ä', ccedil: 'ç',
};
/**
 * A WordPress *_gmt date ("2026-09-17T09:11:41", UTC without a zone) in ISO 8601 with the
 * zone, as structured data wants it; '' when missing or invalid.
 */
function isoFromGmt(gmt?: string): string {
    const d = gmt ? new Date(`${gmt}Z`) : null;
    return d && !isNaN(d.getTime()) ? d.toISOString().replace(/\.\d{3}Z$/, '+00:00') : '';
}

// Curly quotes become straight ones, as the site has always shown them.
const STRAIGHT_QUOTES: Record<number, string> = { 8216: "'", 8217: "'", 8220: '"', 8221: '"' };

/**
 * Decode HTML entities from WordPress (e.g. &#8217; → ', &hellip; → …, &amp; → &), in one
 * pass so an escaped entity such as &amp;lt; stays the text "&lt;".
 */
function decodeHTMLEntities(text: string): string {
    return text.replace(/&(?:#(\d+)|#x([0-9a-f]+)|([a-z][a-z0-9]*));/gi, (entity, dec, hex, name) => {
        if (name) return Object.prototype.hasOwnProperty.call(NAMED_ENTITIES, name) ? NAMED_ENTITIES[name] : entity;
        const code = dec ? parseInt(dec, 10) : parseInt(hex, 16);
        if (STRAIGHT_QUOTES[code]) return STRAIGHT_QUOTES[code];
        return code > 0 && code <= 0x10ffff ? String.fromCodePoint(code) : entity;
    });
}

/**
 * Card excerpt (blog posts, case studies): up to max characters, cut between words, with one
 * ellipsis. Text that fits is returned unchanged (WordPress already ends a trimmed excerpt
 * with "…").
 */
export function clip(text: string, max = 140): string {
    if (text.length <= max) return text;
    const cut = text.slice(0, max + 1);
    const end = cut.lastIndexOf(' ');
    return (end > 0 ? cut.slice(0, end) : text.slice(0, max)).replace(/[\s.,;:…-]+$/, '') + '…';
}

/**
 * Job descriptions typed as plain text (line breaks, no paragraph markup) would otherwise
 * render as one block. Blank lines separate blocks. A block of one line is a paragraph; a
 * block of several plain lines is a list (after a first line that is a label, such as
 * "What you bring:" or a bold heading); lines starting with -, • or * are list items and
 * the lines around them paragraphs. Inline markup the editor typed (<strong>, &amp;) is kept;
 * a stray < or & is escaped.
 */
function formatPlainText(raw: string): string {
    if (!raw.trim() || /<(p|ul|ol|li|h[1-6]|div|br|table|blockquote)\b/i.test(raw)) return raw;
    const BULLET = /^[-•*]\s+/;
    const LABEL = /:$|^<(strong|b)>[^<]*<\/\1>$/i;
    const list = (items: string[]) => `<ul>${items.map((t) => `<li>${t}</li>`).join('')}</ul>`;
    const safe = raw
        .replace(/\r\n?/g, '\n')
        .replace(/&(?!#\d+;|#x[0-9a-f]+;|[a-z][a-z0-9]*;)/gi, '&amp;')
        .replace(/<(?![a-z/])/gi, '&lt;');

    return safe.split(/\n\s*\n/).map((block) => {
        const lines = block.split('\n').map((l) => l.trim()).filter(Boolean);
        if (!lines.some((l) => BULLET.test(l))) {
            if (lines.length < 2) return lines.length ? `<p>${lines[0]}</p>` : '';
            const label = lines.length > 2 && LABEL.test(lines[0]) ? `<p>${lines.shift()}</p>` : '';
            return label + list(lines);
        }
        let html = '';
        let items: string[] = [];
        for (const line of lines) {
            if (BULLET.test(line)) { items.push(line.replace(BULLET, '')); continue; }
            if (items.length) { html += list(items); items = []; }
            html += `<p>${line}</p>`;
        }
        return items.length ? html + list(items) : html;
    }).join('\n');
}

// Pages of this site a blog post may link to, as paths without the trailing slash. Blog
// posts come from WordPress; solutions, guides and services from the same (approval-gated)
// data their routes are built from; the rest are the fixed pages in src/pages.
const FIXED_PAGES = [
    '', '/about', '/about/partners', '/blog', '/careers', '/contact', '/guides', '/industries',
    '/privacy', '/resources', '/resources/case-studies', '/resources/faq', '/services',
    '/solutions', '/terms',
    // src/pages/industries/[slug].astro
    '/industries/technology', '/industries/life-sciences', '/industries/finance',
    '/industries/professional-services', '/industries/logistics', '/industries/ngo',
    '/industries/manufacturing', '/industries/industrial',
];

function sitePaths(blogSlugs: string[]): Set<string> {
    return new Set([
        ...FIXED_PAGES,
        ...blogSlugs.map((s) => `/blog/${s}`),
        ...solutions.map((s: any) => `/solutions/${s.slug}`),
        ...[...settlersData, ...teamsData, ...sosData].map((g: any) => `/guides/${g.slug}`),
        ...servicesData.map((s: any) => `/services/${s.slug}`),
    ]);
}

// hrhelp.nl in any form: http or https, with or without www, any case.
const SITE_ORIGIN = /^(?:https?:)?\/\/(?:www\.)?hrhelp\.nl(?=[/?#]|$)/i;

/**
 * Links to this site become site-relative with a trailing slash, so a reader never goes
 * through a 301 (http, no www) or a 308 (no trailing slash) to reach the page. Only links to
 * pages that exist in this build are rewritten; anything else is left exactly as written.
 */
function normaliseSiteLinks(html: string, paths: Set<string>): string {
    return html.replace(/(<a\b[^>]*?\shref=)(["'])(.*?)\2/gi, (tag, start, quote, href) => {
        let local = href;
        if (SITE_ORIGIN.test(href)) {
            local = href.replace(SITE_ORIGIN, '');
            if (!local.startsWith('/')) local = '/' + local;
        }
        if (!local.startsWith('/') || local.startsWith('//')) return tag;
        const cut = local.search(/[?#]/);
        const key = (cut < 0 ? local : local.slice(0, cut)).replace(/\/+$/, '');
        if (!paths.has(key)) return tag;
        return start + quote + key + '/' + (cut < 0 ? '' : local.slice(cut)) + quote;
    });
}

/**
 * Fetch from WP REST API.
 * Tries pretty permalinks first (/wp-json/wp/v2/), falls back to ?rest_route= format.
 */
// Per-build memo: the same endpoints (featured articles, post lists) are requested by
// every page during a static build. One network call per endpoint per build is enough;
// the cache-buster below still guarantees fresh content on every new build.
const buildMemo = new Map<string, Promise<unknown>>();

async function wpFetch<T>(endpoint: string): Promise<T | null> {
    if (!WP_URL) return null;
    if (!buildMemo.has(endpoint)) {
        buildMemo.set(endpoint, wpFetchUncached<T>(endpoint));
    }
    return buildMemo.get(endpoint) as Promise<T | null>;
}

// Waits before the 2nd, 3rd and 4th try of a request that failed in a way that can pass:
// a rate limit (429, which the WP host does send during builds), a 5xx, a timeout or an
// unreachable host.
const RETRY_WAITS_MS = [1000, 3000, 6000];
const WP_TIMEOUT_MS = 20000;

type WPAttempt = { data: unknown } | { problem: string; retry: boolean; waitMs?: number };

// One try: the pretty URL, and the ?rest_route= form when that answers 404 or cannot connect.
async function wpAttempt(urls: string[]): Promise<WPAttempt> {
    let problem = '';
    let retry = false;
    for (const url of urls) {
        let res: Response;
        try {
            res = await fetch(url, {
                headers: {
                    'Accept': 'application/json',
                    'Cache-Control': 'no-cache, no-store',
                },
                signal: AbortSignal.timeout(WP_TIMEOUT_MS),
            });
        } catch (err) {
            problem = `unreachable (${(err as Error).message})`;
            retry = true;
            continue;
        }
        if (res.status === 404) {
            problem = 'HTTP 404';
            continue;
        }
        if (!res.ok) {
            const retryAfter = Number(res.headers.get('retry-after'));
            return {
                problem: `HTTP ${res.status}`,
                retry: res.status === 429 || res.status >= 500,
                waitMs: retryAfter > 0 ? Math.min(retryAfter, 30) * 1000 : undefined,
            };
        }
        try {
            return { data: await res.json() };
        } catch {
            return { problem: `HTTP ${res.status} with a body that is not JSON`, retry: true };
        }
    }
    return { problem, retry };
}

async function wpFetchUncached<T>(endpoint: string): Promise<T | null> {

    // Cache-buster: the WP hosting aggressively caches REST API responses.
    // A unique timestamp on each build ensures we always get fresh content.
    const cacheBuster = `_nocache=${Date.now()}`;
    const separator = endpoint.includes('?') ? '&' : '?';
    const bustEndpoint = `${endpoint}${separator}${cacheBuster}`;

    const prettyUrl = `${WP_URL}/wp-json/wp/v2/${bustEndpoint}`;
    const queryUrl = `${WP_URL}/?rest_route=/wp/v2/${bustEndpoint}`;

    let attempt = await wpAttempt([prettyUrl, queryUrl]);
    for (const wait of RETRY_WAITS_MS) {
        if ('data' in attempt || !attempt.retry) break;
        const ms = attempt.waitMs ?? wait;
        console.warn(`[WP] ${endpoint}: ${attempt.problem}, retrying in ${ms / 1000}s`);
        await new Promise((resolve) => setTimeout(resolve, ms));
        attempt = await wpAttempt([prettyUrl, queryUrl]);
    }
    if ('data' in attempt) return attempt.data as T;

    // Falling back here would publish the 3 fallback posts and no job openings, dropping every
    // other blog and careers URL, so a production build stops instead.
    const failure = `[WP] Could not fetch ${endpoint} from ${WP_URL}: ${attempt.problem}.`;
    if (ALLOW_FALLBACK) {
        console.warn(`${failure} Using fallback content (WP_ALLOW_FALLBACK=1).`);
        return null;
    }
    throw new Error(`${failure} Build stopped so the last good deploy stays live. Set WP_ALLOW_FALLBACK=1 to build with fallback content (local development only).`);
}

// ---------- WP → APP TYPE MAPPERS ----------

function mapWPCaseStudy(post: any): CaseStudy {
    const acf = post.acf || {};
    return {
        slug: post.slug,
        tag: acf.tag || '',
        title: post.title?.rendered || '',
        intro: acf.intro || '',
        icon: acf.icon || 'article',
        color: acf.color || 'var(--orange)',
        image: acf.image || '',
        illustration: acf.illustration || '',
        items: (acf.approach_items || []).map((item: any) => item.text || item),
        outcome: acf.outcome || '',
        stats: (acf.stats || []).map((s: any) => ({ value: s.value, label: s.label })),
        floatCards: acf.float_cards || { tl: { icon: '', label: '', value: '' }, br: { icon: '', label: '', value: '' } },
        context: acf.context || '',
    };
}

function mapWPExpertise(post: any): Expertise {
    const acf = post.acf || {};
    return {
        slug: post.slug,
        title: post.title?.rendered || '',
        subtitle: acf.subtitle || '',
        tagline: acf.tagline || '',
        icon: acf.icon || 'work',
        image: acf.image || '',
        illustration: acf.illustration || '',
        intro: acf.intro || '',
        floatCards: acf.float_cards || { tl: { icon: '', label: '', value: '' }, br: { icon: '', label: '', value: '' } },
        premiseHeading: acf.premise_heading || '',
        premiseBody: acf.premise_body ? (Array.isArray(acf.premise_body) ? acf.premise_body : acf.premise_body.split('\n\n')) : [],
        included: (acf.included || []).map((item: any) => ({ title: item.title, desc: item.desc || item.description })),
        result: acf.result || '',
        stats: (acf.stats || []).map((s: any) => ({ value: s.value, label: s.label })),
    };
}

function mapWPFAQGroup(post: any): FAQGroup {
    const acf = post.acf || {};
    return {
        category: post.title?.rendered || acf.category || '',
        items: (acf.items || []).map((item: any) => ({
            q: item.question || item.q || '',
            a: item.answer || item.a || '',
        })),
    };
}

function mapWPBlogPost(post: any, paths: Set<string>): BlogPost {
    const acf = post.acf || {};
    // Strip HTML tags from excerpt
    const rawExcerpt = post.excerpt?.rendered || acf.excerpt || '';
    const cleanExcerpt = rawExcerpt.replace(/<[^>]*>/g, '').trim();
    // WordPress ends a trimmed excerpt with " [&hellip;]"; a plain ellipsis reads better
    // in the intro, the meta description and the share cards. A full stop before it goes,
    // so a sentence that ended there shows one ellipsis instead of ".…".
    const excerpt = decodeHTMLEntities(cleanExcerpt).replace(/[\s.]*\[(?:…|\.\.\.)\]\s*$/, '…');

    // Get featured image from _embedded media (standard WP) or fall back to ACF
    let imageUrl = acf.featured_image || '/images/dutch-business.jpg';
    const embedded = post._embedded?.['wp:featuredmedia'];
    if (embedded && embedded.length > 0 && embedded[0]?.source_url) {
        imageUrl = embedded[0].source_url;
    }

    // Fix broken internal links in WP content at build time
    let content = post.content?.rendered || acf.content || '';
    const linkFixes: Record<string, string> = {
        '/resources/blog/': '/blog/',
        '/solutions/compliance-advisory': '/solutions/hr-reset',
        '/solutions/hr-outsourcing': '/solutions/hr-teams',
        '/solutions/market-entry': '/solutions/hr-settlers',
        '/solutions/payroll-administration': '/solutions/hr-teams',
        '/solutions/recruitment-support': '/solutions/hr-settlers',
        '/industries/technology-saas': '/industries/technology',
        // Old expertise overview (exact href, so detail-page links are left alone)
        'href="/resources/expertise"': 'href="/services/#core-expertise"',
    };
    for (const [wrong, correct] of Object.entries(linkFixes)) {
        content = content.replaceAll(wrong, correct);
    }
    content = normaliseSiteLinks(content, paths);

    // Fix empty alt attributes in WP content images at build time
    const postTitle = decodeHTMLEntities(post.title?.rendered || 'HRHelp article image');
    content = content.replace(/alt=""/g, `alt="${postTitle}"`);

    return {
        slug: post.slug,
        title: decodeHTMLEntities(post.title?.rendered || ''),
        excerpt,
        content,
        category: (() => {
            // Use WordPress native categories from _embedded (the ones set in the editor sidebar)
            const terms = post._embedded?.['wp:term'];
            if (terms && terms[0] && terms[0].length > 0) {
                const cats = terms[0]
                    .filter((t: any) => t.name !== 'Uncategorized')
                    .map((t: any) => decodeHTMLEntities(t.name));
                if (cats.length > 0) return cats;
            }
            // Fallback to ACF field or default
            return [acf.blog_category || 'Article'];
        })(),
        image: imageUrl,
        date: post.date ? new Date(post.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : '',
        modified: post.modified ? new Date(post.modified).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : '',
        datePublished: isoFromGmt(post.date_gmt),
        dateModified: isoFromGmt(post.modified_gmt),
        readTime: acf.read_time || '5 min read',
        author: acf.author_name || 'HRHelp Team',
        tags: (() => {
            const cats = (post._embedded?.['wp:term']?.[0] || [])
                .filter((t: any) => t.name !== 'Uncategorized')
                .map((t: any) => decodeHTMLEntities(t.name));
            if (cats.length > 0) return cats;
            return acf.blog_category ? [acf.blog_category] : [];
        })(),
    };
}

// ---------- PUBLIC API ----------

/**
 * Get all case studies. Falls back to hardcoded data if WP is unavailable.
 */
export async function getCaseStudies(): Promise<CaseStudy[]> {
    const posts = await wpFetch<any[]>('case_study?per_page=100&_fields=id,slug,title,acf');
    if (posts && posts.length > 0) {
        return posts.map(mapWPCaseStudy);
    }
    return fallbackCaseStudies;
}

/**
 * Get a single case study by slug. Falls back to hardcoded data if WP is unavailable.
 */
export async function getCaseStudy(slug: string): Promise<CaseStudy | null> {
    // The list request (made once per build) already holds every case study in full.
    const listed = (await getCaseStudies()).find(cs => cs.slug === slug);
    if (listed) return listed;
    const posts = await wpFetch<any[]>(`case_study?slug=${slug}&_fields=id,slug,title,acf`);
    if (posts && posts.length > 0) {
        return mapWPCaseStudy(posts[0]);
    }
    return fallbackCaseStudies.find(cs => cs.slug === slug) || null;
}

/**
 * Get all expertise items. Falls back to hardcoded data if WP is unavailable.
 */
export async function getExpertiseItems(): Promise<Expertise[]> {
    const posts = await wpFetch<any[]>('expertise?per_page=100&_fields=id,slug,title,acf');
    if (posts && posts.length > 0) {
        return posts.map(mapWPExpertise);
    }
    return fallbackExpertise;
}

/**
 * Get a single expertise item by slug. Falls back to hardcoded data if WP is unavailable.
 */
export async function getExpertiseItem(slug: string): Promise<Expertise | null> {
    // The list request (made once per build) already holds every expertise item in full.
    const listed = (await getExpertiseItems()).find(e => e.slug === slug);
    if (listed) return listed;
    const posts = await wpFetch<any[]>(`expertise?slug=${slug}&_fields=id,slug,title,acf`);
    if (posts && posts.length > 0) {
        return mapWPExpertise(posts[0]);
    }
    return fallbackExpertise.find(e => e.slug === slug) || null;
}

/**
 * Get all FAQ groups. Falls back to hardcoded data if WP is unavailable.
 */
export async function getFAQGroups(): Promise<FAQGroup[]> {
    const posts = await wpFetch<any[]>('faq_group?per_page=100&orderby=menu_order&order=asc&_fields=id,slug,title,acf');
    if (posts && posts.length > 0) {
        return posts.map(mapWPFAQGroup);
    }
    return fallbackFAQGroups;
}

/**
 * Get all blog posts. Uses WP native 'posts' endpoint.
 */
// Every page asks for the post list (header, homepage, blog); it is fetched and mapped once.
// Each caller still gets its own array, so sorting or slicing it touches nobody else's.
let blogPostsMemo: Promise<BlogPost[]> | null = null;

export async function getBlogPosts(): Promise<BlogPost[]> {
    if (!blogPostsMemo) blogPostsMemo = loadBlogPosts();
    return (await blogPostsMemo).slice();
}

async function loadBlogPosts(): Promise<BlogPost[]> {
    const posts = await wpFetch<any[]>('posts?per_page=100&_embed');
    if (posts && posts.length > 0) {
        console.log(`[WP Blog] Fetched ${posts.length} posts: ${posts.map((p: any) => p.slug).join(', ')}`);
        const paths = sitePaths(posts.map((p: any) => p.slug));
        return posts.map((p: any) => mapWPBlogPost(p, paths));
    }
    console.warn('[WP Blog] No posts returned from API, using fallback');
    return fallbackBlogPosts;
}

/**
 * Get a single blog post by slug. The post list already holds every post in full, so a
 * request of its own is only needed past the first 100 posts.
 */
export async function getBlogPost(slug: string): Promise<BlogPost | null> {
    const all = await getBlogPosts();
    const listed = all.find(p => p.slug === slug);
    if (listed) return listed;
    const posts = await wpFetch<any[]>(`posts?slug=${slug}&_embed`);
    if (posts && posts.length > 0) {
        return mapWPBlogPost(posts[0], sitePaths([...all.map(p => p.slug), slug]));
    }
    return fallbackBlogPosts.find(p => p.slug === slug) || null;
}

/**
 * Get featured articles for the header dropdown (latest 3 blog posts).
 */
export async function getFeaturedArticles(): Promise<{ title: string; category: string; image: string; href: string }[]> {
    const posts = await getBlogPosts();
    return posts.slice(0, 3).map((p: BlogPost) => ({
        title: p.title,
        category: p.category[0] || 'Article',
        image: p.image,
        href: `/blog/${p.slug}/`,
    }));
}

// ---------- JOB OPENINGS ----------

// Places job posts name, for the JobPosting location: cities in the location field, title or
// text, plus regions and countries in the location field that no city already covers.
const JOB_CITIES = [
    { re: /capelle aan den ijssel/i, locality: 'Capelle aan den IJssel', country: 'NL' },
    { re: /\bamsterdam\b/i, locality: 'Amsterdam', country: 'NL' },
    { re: /\balmere\b/i, locality: 'Almere', country: 'NL' },
    { re: /\btelford\b/i, locality: 'Telford', country: 'GB' },
];
const JOB_REGIONS = [{ re: /\brandstad\b/i, region: 'Randstad', country: 'NL' }];
const JOB_COUNTRIES = [
    { re: /\b(nl|netherlands|nederland)\b/i, country: 'NL' },
    { re: /\b(uk|united kingdom|england|gb)\b/i, country: 'GB' },
];

function jobPlaces(location: string, text: string): JobPlace[] {
    const places: JobPlace[] = JOB_CITIES
        .filter((c) => c.re.test(`${location} ${text}`))
        .map(({ locality, country }) => ({ locality, country }));
    for (const { re, region, country } of JOB_REGIONS) {
        if (re.test(location)) places.push({ region, country });
    }
    for (const { re, country } of JOB_COUNTRIES) {
        if (re.test(location) && !places.some((p) => p.country === country)) places.push({ country });
    }
    return places;
}

function mapWPJobOpening(post: any): JobOpening {
    const acf = post.acf || {};
    const title = decodeHTMLEntities(post.title?.rendered || '');
    const location = (acf.location || '').trim();
    const description = formatPlainText(acf.job_description || '');
    return {
        slug: post.slug || '',
        title,
        type: acf.job_type || 'Full-Time',
        location: location || 'Amsterdam, Netherlands',
        description,
        datePosted: isoFromGmt(post.date_gmt),
        places: jobPlaces(location, `${title} ${description}`),
        // Only a location of just "Remote": jobs that are partly on site are not TELECOMMUTE for Google
        remote: /^(fully\s+)?remote$/i.test(location),
    };
}

/**
 * Get all active job openings. Falls back to hardcoded data if WP is unavailable.
 */
export async function getJobOpenings(): Promise<JobOpening[]> {
    const posts = await wpFetch<any[]>('job_opening?per_page=100&_fields=id,slug,title,acf,status,date_gmt');
    if (posts && posts.length > 0) {
        return posts
            .filter(p => {
                const active = p.acf?.is_active;
                return active !== 'false' && active !== 'no' && active !== '0' && active !== false;
            })
            .map(mapWPJobOpening);
    }
    return fallbackJobOpenings;
}

/**
 * Get a single job opening by slug.
 */
export async function getJobOpening(slug: string): Promise<JobOpening | null> {
    const posts = await wpFetch<any[]>(`job_opening?slug=${slug}&_fields=id,slug,title,acf,date_gmt`);
    if (posts && posts.length > 0) {
        return mapWPJobOpening(posts[0]);
    }
    return fallbackJobOpenings.find(j => j.slug === slug) || null;
}
