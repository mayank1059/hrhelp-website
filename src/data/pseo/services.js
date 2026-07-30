import services from './services.json';
import approved from './approved-services.json';

// Same gating pattern as guides.js:
// - Staging (PUBLIC_STAGING=true): show ALL service pages for client review.
// - Production: show only approved ones (approved-services.json).
const isStaging = import.meta.env.PUBLIC_STAGING === 'true';
const approvedSet = new Set(approved);
export const servicesData = isStaging ? services : services.filter((s) => approvedSet.has(s.slug));
