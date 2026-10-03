import { servicesData } from './services.js';

// Single source of truth for how the 11 service pages are grouped and labelled.
// Used by the services index, the header mega menus and the homepage services band.
// servicesData is already staging-gated, so unapproved services never appear on production.

// Compact labels for navigation and chip lists (pages keep their full names).
const shortNames = {
  'interim-hr-solutions': 'Interim HR Solutions',
  'fractional-hr-solutions': 'Fractional HR Solutions',
  'temporary-hr-solutions': 'Temporary HR Solutions',
  'interim-hr-support': 'Interim HR Support',
  'interim-hr-manager': 'Interim HR Manager',
  'fractional-hr-manager': 'Fractional HR Manager',
  'interim-hr-advisor': 'Interim HR Advisor',
  'hr-consultancy-foreign-companies': 'HR Consultancy',
  'hr-compliance-dutch-entity-foreign-company': 'Dutch Entity Compliance',
  'labor-law-advice-international-employer': 'Dutch Labour Law Advice',
  'hr-recruitment-netherlands': 'HR Recruitment',
};

const decorate = (s) => ({ ...s, short: shortNames[s.slug] || s.name });

export const serviceGroupDefs = [
  {
    label: 'Flexible HR Capacity',
    desc: 'Senior HR hands for a gap, a project or a busy period.',
    icon: 'clock',
    slugs: ['interim-hr-solutions', 'fractional-hr-solutions', 'temporary-hr-solutions', 'interim-hr-support'],
  },
  {
    label: 'Embedded HR Roles',
    desc: 'A named HR manager or advisor inside your team.',
    icon: 'user',
    slugs: ['interim-hr-manager', 'fractional-hr-manager', 'interim-hr-advisor'],
  },
  {
    label: 'For Foreign Companies',
    desc: 'Dutch compliance, labour law and hiring for employers based abroad.',
    icon: 'globe',
    slugs: ['hr-consultancy-foreign-companies', 'hr-compliance-dutch-entity-foreign-company', 'labor-law-advice-international-employer', 'hr-recruitment-netherlands'],
  },
];

export const serviceGroups = serviceGroupDefs
  .map((g) => ({
    ...g,
    items: g.slugs
      .map((slug) => servicesData.find((s) => s.slug === slug))
      .filter(Boolean)
      .map(decorate),
  }))
  .filter((g) => g.items.length > 0);

// Every visible service, in group order, decorated with its short label.
export const serviceLinks = serviceGroups.flatMap((g) => g.items);

// Services that belong to a solution package, e.g. servicesForSolution('hr-teams').
export function servicesForSolution(solutionSlug) {
  const path = `/solutions/${solutionSlug}/`;
  return serviceLinks.filter((s) => s.parentService === path);
}
