// /build-info.json: what this build was made from. The scheduled check in CI
// (scripts/wp-changed.mjs) compares it with WordPress to decide whether the site needs a rebuild.
// Endpoints are not pages, so it stays out of the sitemap.
import type { APIRoute } from 'astro';
import { getWpState } from '../../scripts/wp-state.mjs';

export const GET: APIRoute = async () => {
    // When `astro build` started: every page fetched its WordPress content after this moment.
    const buildStart = Date.now() - process.uptime() * 1000;

    let wp = null;
    try {
        wp = await getWpState(import.meta.env.PUBLIC_WP_URL);
    } catch (err) {
        // Without these values the next check rebuilds, and that build writes them again.
        console.warn(`[build-info] WordPress state not recorded: ${(err as Error).message}`);
    }

    // A change saved while this build ran may be missing from its pages, so the date recorded
    // never passes the build start: the next check then sees that change as newer and rebuilds once.
    let wpLastModified = wp?.lastModified ?? null;
    if (wpLastModified && Date.parse(wpLastModified) > buildStart) {
        wpLastModified = new Date(buildStart).toISOString();
    }

    const info = {
        buildTime: new Date(buildStart).toISOString(),
        commit: process.env.GITHUB_SHA || null,
        wpLastModified,
        wpCounts: wp?.counts ?? null,
    };
    return new Response(JSON.stringify(info, null, 2) + '\n', {
        headers: { 'Content-Type': 'application/json' },
    });
};
