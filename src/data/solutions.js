// The four core solution packages, shared by the cross-linking blocks.
export const solutions = [
  { slug: 'hr-settlers', name: 'HR Settlers', tagline: 'Enter the Dutch market with confidence' },
  { slug: 'hr-teams', name: 'HR Teams', tagline: 'Your outsourced HR department' },
  { slug: 'hr-reset', name: 'HR Reset', tagline: 'Modernise your existing HR' },
  { slug: 'hr-sos', name: 'HR S.O.S.', tagline: 'Urgent HR crisis support' },
];

export const solutionBySlug = Object.fromEntries(solutions.map((s) => [s.slug, s]));
