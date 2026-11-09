import settlers from './hr-settlers.json';
import teams from './hr-teams.json';
import sos from './hr-sos.json';
import approved from './approved-guides.json';
import scheduled from './scheduled-guides.json';

// Single source of truth for which guides are visible.
// - Staging (PUBLIC_STAGING=true): show ALL guides so the client can review them.
// - Production: show only client-approved guides (see approved-guides.json).
// This keeps "approved = live" baked into the build, so CI deploys can never
// accidentally drop approved guides or publish unapproved ones.
const isStaging = import.meta.env.PUBLIC_STAGING === 'true';
// Approved guides with a publish date (scheduled-guides.json) go live from that date
// (Amsterdam time); .github/workflows/scheduled-guides.yml rebuilds the site on those days.
const today = new Date().toLocaleDateString('en-CA', { timeZone: 'Europe/Amsterdam' });
const approvedSet = new Set([...approved, ...scheduled.filter((g) => g.publish <= today).map((g) => g.slug)]);
const filterApproved = (arr) => (isStaging ? arr : arr.filter((g) => approvedSet.has(g.slug)));

export const settlersData = filterApproved(settlers);
export const teamsData = filterApproved(teams);
export const sosData = filterApproved(sos);
