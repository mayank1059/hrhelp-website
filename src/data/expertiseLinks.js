// Core expertise topic cluster: which of the three expertise pages a solution,
// service, guide or blog page links to (the "Core expertise" block,
// CoreExpertiseLinks.astro). First slug = closest match.

export const coreExpertise = {
  'sickness-management': {
    title: 'Sickness Management',
    line: 'Absence policy, Wet Poortwachter compliance and manager coaching that keep sickness under control.',
  },
  restructuring: {
    title: 'Restructuring',
    line: 'Reorganisations, redundancies and site closures, handled correctly with the works council, the UWV and your people.',
  },
  'leadership-training': {
    title: 'Leadership Training',
    line: 'Hands-on training that helps managers see how culture shapes the way they lead and work together.',
  },
};

// Solution and service pages, by slug
const pageTopics = {
  // Solutions
  'hr-sos': ['restructuring', 'sickness-management'],
  'hr-teams': ['sickness-management', 'leadership-training'],
  'hr-reset': ['restructuring'],
  'hr-settlers': ['leadership-training'],
  // Services
  'interim-hr-solutions': ['sickness-management'],
  'interim-hr-support': ['sickness-management'],
  'interim-hr-advisor': ['sickness-management'],
  'interim-hr-manager': ['restructuring', 'sickness-management'],
  'fractional-hr-solutions': ['sickness-management'],
  'fractional-hr-manager': ['leadership-training', 'sickness-management'],
  'temporary-hr-solutions': ['restructuring'],
  'labor-law-advice-international-employer': ['restructuring', 'sickness-management'],
  'hr-compliance-dutch-entity-foreign-company': ['sickness-management'],
  'hr-consultancy-foreign-companies': ['leadership-training'],
};

// Guides and blog posts: keywords in the slug
const slugKeywords = [
  ['sickness-management', /sick|absence|poortwachter|verzuim/],
  ['restructuring', /restructur|redundan|dismiss|reorgan|works-council|collective|terminat|settlement/],
  ['leadership-training', /leadership|manager|culture|performance|feedback/],
];

export const expertiseForPage = (slug) => pageTopics[slug] || [];

export const expertiseForSlug = (slug) =>
  slugKeywords.filter(([, re]) => re.test(slug)).map(([expertise]) => expertise);
