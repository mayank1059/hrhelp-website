// Has the WordPress content changed since the build that is live? Used by the detect job in
// .github/workflows/deploy.yml: writes changed=true|false to $GITHUB_OUTPUT (and prints it).
//   - WordPress cannot be read: changed=false, with a warning. A build would fail on it anyway,
//     and the next check tries again.
//   - The live build-info.json does not exist (HTTP 404): changed=true, so a build writes one.
//   - It cannot be read otherwise (challenge page, 403/5xx, timeout): changed=false, with a
//     warning, so a blocked check never deploys every 10 minutes.
//   - Signal and scheduled runs pass EXPECTED_COMMIT (main's newest commit): when the live build is another
//     commit (a push deploy that was cancelled while pending, or failed), deploy it.
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
    if (res.status === 404) return null;
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const info = await res.json(); // an HTML challenge page served with 200 throws here
    if (!info || typeof info !== 'object') throw new Error('not a build-info object');
    return info;
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
        return [false, `${BUILD_INFO_URL} could not be read (${err.message}); not deploying this time.`, 'warning'];
    }
    if (!live) return [true, `${BUILD_INFO_URL} does not exist yet (HTTP 404); deploying.`, 'notice'];

    const reasons = [];
    if (!(Date.parse(live?.wpLastModified) >= Date.parse(wp.lastModified))) {
        reasons.push(`last modified ${wp.lastModified}, live build has ${live?.wpLastModified ?? 'no date'}`);
    }
    for (const [type, count] of Object.entries(wp.counts)) {
        const liveCount = live?.wpCounts?.[type];
        if (liveCount !== count) reasons.push(`${type}: ${count} published, live build has ${liveCount ?? 'no count'}`);
    }
    // Scheduled runs: main's newest commit is not live (a push run cancelled while pending, or failed).
    const expected = process.env.EXPECTED_COMMIT;
    if (expected && live.commit !== expected) reasons.push(`main is at ${expected}, live build has ${live.commit ?? 'no commit'}`);
    if (reasons.length) return [true, `The live build is out of date (${reasons.join('; ')}); deploying.`, 'notice'];
    return [false, `WordPress unchanged since the live build (last modified ${wp.lastModified}); nothing to deploy.`, 'notice'];
}

const [changed, message, level] = await check();
console.log(`::${level}::${message}`);
console.log(`changed=${changed}`);
if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `changed=${changed}\n`);
