// Has the WordPress content changed since the build that is live? Used by the detect job in
// .github/workflows/deploy.yml: writes changed=true|false to $GITHUB_OUTPUT (and prints it).
//   - WordPress cannot be read: changed=false, with a warning. A build would fail on it anyway,
//     and the next check tries again.
//   - The live build-info.json is missing or unreadable: changed=true, so a build writes one.
// Env: PUBLIC_WP_URL (as for the build); BUILD_INFO_URL to read another build-info.json than
// production's (for testing).
//
// Run: PUBLIC_WP_URL=https://admin.hrhelp.nl node scripts/wp-changed.mjs

import { appendFileSync } from 'node:fs';
import { getWpState } from './wp-state.mjs';

const BUILD_INFO_URL = process.env.BUILD_INFO_URL || 'https://www.hrhelp.nl/build-info.json';

async function liveBuildInfo() {
    const url = new URL(BUILD_INFO_URL);
    url.searchParams.set('t', Date.now()); // past any CDN cache
    const res = await fetch(url, { headers: { 'Cache-Control': 'no-cache' }, signal: AbortSignal.timeout(20000) });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
}

// Returns [changed, message, annotation level].
async function check() {
    let wp;
    try {
        wp = await getWpState(process.env.PUBLIC_WP_URL);
    } catch (err) {
        return [false, `WordPress could not be read (${err.message}); not deploying this time.`, 'warning'];
    }

    let live;
    try {
        live = await liveBuildInfo();
    } catch (err) {
        return [true, `No readable ${BUILD_INFO_URL} (${err.message}); deploying.`, 'notice'];
    }

    const reasons = [];
    if (!(Date.parse(live?.wpLastModified) >= Date.parse(wp.lastModified))) {
        reasons.push(`last modified ${wp.lastModified}, live build has ${live?.wpLastModified ?? 'no date'}`);
    }
    for (const [type, count] of Object.entries(wp.counts)) {
        const liveCount = live?.wpCounts?.[type];
        if (liveCount !== count) reasons.push(`${type}: ${count} published, live build has ${liveCount ?? 'no count'}`);
    }
    if (reasons.length) return [true, `WordPress changed since the live build (${reasons.join('; ')}); deploying.`, 'notice'];
    return [false, `WordPress unchanged since the live build (last modified ${wp.lastModified}); nothing to deploy.`, 'notice'];
}

const [changed, message, level] = await check();
console.log(`::${level}::${message}`);
console.log(`changed=${changed}`);
if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `changed=${changed}\n`);
