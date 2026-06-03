import settlers from './hr-settlers.json';
import teams from './hr-teams.json';
import sos from './hr-sos.json';
import approved from './approved-guides.json';

// Single source of truth for which guides are visible.
// - Staging (PUBLIC_STAGING=true): show ALL guides so the client can review them.
// - Production: show only client-approved guides (see approved-guides.json).
// This keeps "approved = live" baked into the build, so CI deploys can never
// accidentally drop approved guides or publish unapproved ones.
const isStaging = import.meta.env.PUBLIC_STAGING === 'true';
const approvedSet = new Set(approved);
const filterApproved = (arr) => (isStaging ? arr : arr.filter((g) => approvedSet.has(g.slug)));

export const settlersData = filterApproved(settlers);
export const teamsData = filterApproved(teams);
export const sosData = filterApproved(sos);
