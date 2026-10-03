// The state of the WordPress content the site is built from, per post type: when it last
// changed (the newest modified_gmt) and how many items are published. The build stores it in
// /build-info.json (src/pages/build-info.json.ts); the scheduled check in CI
// (scripts/wp-changed.mjs) compares the live file with WordPress to decide whether to rebuild.
// The counts catch what a date cannot: an item deleted or unpublished, or a scheduled post
// going live (WordPress publishes it without changing its modified date).

// Every post type src/lib/wordpress.ts fetches. Keep the two in step.
export const WP_TYPES = ['posts', 'case_study', 'expertise', 'faq_group', 'job_opening'];

// Waits before the 2nd, 3rd and 4th try: the WP host answers 429 under load.
const RETRY_WAITS_MS = [2000, 5000, 10000];

// One post type, through the pretty REST URL or else the ?rest_route= form, as
// src/lib/wordpress.ts does. The cache-buster gets past the host's REST cache.
async function readType(wpUrl, type) {
    const query = `per_page=1&orderby=modified&order=desc&_fields=modified_gmt&_nocache=${Date.now()}`;
    let problem = '';
    for (const url of [`${wpUrl}/wp-json/wp/v2/${type}?${query}`, `${wpUrl}/?rest_route=/wp/v2/${type}&${query}`]) {
        try {
            const res = await fetch(url, {
                headers: { 'Accept': 'application/json', 'Cache-Control': 'no-cache, no-store' },
                signal: AbortSignal.timeout(20000),
            });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            const items = await res.json();
            const count = parseInt(res.headers.get('x-wp-total'), 10);
            if (!Array.isArray(items) || !Number.isInteger(count)) throw new Error('unexpected answer');
            return { count, lastModified: items[0]?.modified_gmt ? `${items[0].modified_gmt}Z` : null };
        } catch (err) {
            problem = err.message;
        }
    }
    throw new Error(`${type}: ${problem}`);
}

async function readTypeWithRetries(wpUrl, type) {
    for (let attempt = 0; ; attempt++) {
        try {
            return await readType(wpUrl, type);
        } catch (err) {
            if (attempt >= RETRY_WAITS_MS.length) throw err;
            await new Promise((resolve) => setTimeout(resolve, RETRY_WAITS_MS[attempt]));
        }
    }
}

/**
 * @param {string | undefined} wpUrl  PUBLIC_WP_URL
 * @returns {Promise<{ lastModified: string, counts: Record<string, number> }>}
 *   lastModified: newest modified_gmt across all types, as ISO 8601 UTC ("2026-09-28T11:55:42Z").
 *   Throws when WordPress cannot be read or has no published content at all.
 */
export async function getWpState(wpUrl) {
    if (!wpUrl) throw new Error('PUBLIC_WP_URL is not set');
    const counts = {};
    let lastModified = null;
    for (const type of WP_TYPES) {
        const state = await readTypeWithRetries(wpUrl, type);
        counts[type] = state.count;
        if (Date.parse(state.lastModified) > (lastModified ? Date.parse(lastModified) : -Infinity)) {
            lastModified = state.lastModified;
        }
    }
    if (!lastModified) throw new Error('WordPress returned no published content');
    return { lastModified, counts };
}
