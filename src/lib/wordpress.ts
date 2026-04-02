/**
 * WordPress Headless CMS API Client
 * Fetches resources content (case studies, expertise, FAQ) from WordPress REST API.
 * Falls back to hardcoded data if WP is unreachable.
 */

import {
    fallbackCaseStudies,
    fallbackExpertise,
    fallbackFAQGroups,
    fallbackResourceHighlights,
    fallbackResourceCaseStudies,
    fallbackBlogPosts,
} from './fallback-data';

// ---------- CONFIG ----------
const WP_URL = import.meta.env.PUBLIC_WP_URL || '';

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

export interface ResourceHighlight {
    title: string;
    desc: string;
    image: string;
    href: string;
    icon: string;
    stat: string;
}

export interface ResourceCaseStudy {
    tag: string;
    title: string;
    desc: string;
    icon: string;
}

export interface BlogPost {
    slug: string;
    title: string;
    excerpt: string;
    content: string;
    category: string;
    image: string;
    date: string;
    readTime: string;
    author: string;
}

// ---------- HELPER ----------

/**
 * Decode HTML entities from WordPress (e.g. &#8217; → ', &amp; → &)
 */
function decodeHTMLEntities(text: string): string {
    return text
        .replace(/&#8217;/g, "'")
        .replace(/&#8216;/g, "'")
        .replace(/&#8220;/g, '"')
        .replace(/&#8221;/g, '"')
        .replace(/&#8211;/g, '–')
        .replace(/&#8212;/g, '—')
        .replace(/&amp;/g, '&')
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&quot;/g, '"')
        .replace(/&#039;/g, "'");
}

/**
 * Fetch from WP REST API.
 * Tries pretty permalinks first (/wp-json/wp/v2/), falls back to ?rest_route= format.
 */
async function wpFetch<T>(endpoint: string): Promise<T | null> {
    if (!WP_URL) return null;

    // Cache-buster: the WP hosting aggressively caches REST API responses.
    // A unique timestamp on each build ensures we always get fresh content.
    const cacheBuster = `_nocache=${Date.now()}`;
    const separator = endpoint.includes('?') ? '&' : '?';
    const bustEndpoint = `${endpoint}${separator}${cacheBuster}`;

    const prettyUrl = `${WP_URL}/wp-json/wp/v2/${bustEndpoint}`;
    const queryUrl = `${WP_URL}/?rest_route=/wp/v2/${bustEndpoint}`;

    for (const url of [prettyUrl, queryUrl]) {
        try {
            const res = await fetch(url, {
                headers: {
                    'Accept': 'application/json',
                    'Cache-Control': 'no-cache, no-store',
                },
            });
            if (res.ok) {
                return await res.json();
            }
            if (res.status !== 404) {
                console.warn(`[WP] Failed to fetch ${endpoint}: ${res.status}`);
                return null;
            }
            // 404 on pretty URL → try query URL
        } catch (err) {
            if (url === prettyUrl) continue;
            console.warn(`[WP] Error fetching ${endpoint}:`, err);
            return null;
        }
    }
    return null;
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

function mapWPBlogPost(post: any): BlogPost {
    const acf = post.acf || {};
    // Strip HTML tags from excerpt
    const rawExcerpt = post.excerpt?.rendered || acf.excerpt || '';
    const cleanExcerpt = rawExcerpt.replace(/<[^>]*>/g, '').trim();

    // Get featured image from _embedded media (standard WP) or fall back to ACF
    let imageUrl = acf.featured_image || '/images/dutch-business.jpg';
    const embedded = post._embedded?.['wp:featuredmedia'];
    if (embedded && embedded.length > 0 && embedded[0]?.source_url) {
        imageUrl = embedded[0].source_url;
    }

    return {
        slug: post.slug,
        title: decodeHTMLEntities(post.title?.rendered || ''),
        excerpt: decodeHTMLEntities(cleanExcerpt),
        content: post.content?.rendered || acf.content || '',
        category: acf.blog_category || 'Article',
        image: imageUrl,
        date: post.date ? new Date(post.date).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : '',
        readTime: acf.read_time || '5 min read',
        author: acf.author_name || 'HRHelp Team',
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
 * Get resource page highlights (derived from expertise items).
 */
export async function getResourceHighlights(): Promise<ResourceHighlight[]> {
    const expertise = await getExpertiseItems();
    if (expertise !== fallbackExpertise) {
        return expertise.map(e => ({
            title: e.title,
            desc: e.intro.slice(0, 120) + '...',
            image: e.image,
            href: `/resources/expertise/${e.slug}`,
            icon: e.icon,
            stat: e.stats.length > 0 ? e.stats[0].value : '',
        }));
    }
    return fallbackResourceHighlights;
}

/**
 * Get resource page case study cards (derived from case studies).
 */
export async function getResourceCaseStudies(): Promise<ResourceCaseStudy[]> {
    const caseStudies = await getCaseStudies();
    if (caseStudies !== fallbackCaseStudies) {
        return caseStudies.map(cs => ({
            tag: cs.tag,
            title: cs.title,
            desc: cs.intro.slice(0, 120) + '...',
            icon: cs.icon,
        }));
    }
    return fallbackResourceCaseStudies;
}

/**
 * Get all blog posts. Uses WP native 'posts' endpoint.
 */
export async function getBlogPosts(): Promise<BlogPost[]> {
    const posts = await wpFetch<any[]>('posts?per_page=100&_embed');
    if (posts && posts.length > 0) {
        console.log(`[WP Blog] Fetched ${posts.length} posts: ${posts.map((p: any) => p.slug).join(', ')}`);
        return posts.map(mapWPBlogPost);
    }
    console.warn('[WP Blog] No posts returned from API, using fallback');
    return fallbackBlogPosts;
}

/**
 * Get a single blog post by slug.
 */
export async function getBlogPost(slug: string): Promise<BlogPost | null> {
    const posts = await wpFetch<any[]>(`posts?slug=${slug}&_embed`);
    if (posts && posts.length > 0) {
        return mapWPBlogPost(posts[0]);
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
        category: p.category,
        image: p.image,
        href: `/blog/${p.slug}`,
    }));
}
