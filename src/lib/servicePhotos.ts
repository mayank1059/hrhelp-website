// Documentary photos for the service pages (public/images/services-photos/).
// The four pages that rank get their own hero and story photos; the rest reuse
// the office set with a different photo per slot.
const P = '/images/services-photos/';
const dims: Record<string, [number, number]> = {
  'office-open-plan': [1200, 675],
  'warehouse-floor': [1200, 800],
  'factory-floor': [1200, 800],
  'office-reception': [1200, 896],
};
export const photo = (n: string, sm = false) => {
  const own = /-(hero|story)$/.test(n);
  const [w, h] = own ? (n.endsWith('-hero') ? [1200, 1200] : [960, 1280]) : (dims[n] || [1200, 900]);
  const k = sm ? 640 / w : 1;
  return { src: `${P}${n}${sm ? '-sm' : ''}.jpg`, width: Math.round(w * k), height: Math.round(h * k) };
};
export const photoSets: Record<string, { hero: string; story: string; process: string }> = {
  'interim-hr-manager': { hero: 'interim-hr-manager-hero', story: 'interim-hr-manager-story', process: 'office-workspace' },
  'hr-consultancy-foreign-companies': { hero: 'hr-consultancy-foreign-companies-hero', story: 'hr-consultancy-foreign-companies-story', process: 'office-entrance-amsterdam' },
  'interim-hr-solutions': { hero: 'interim-hr-solutions-hero', story: 'interim-hr-solutions-story', process: 'office-collaboration' },
  'fractional-hr-manager': { hero: 'fractional-hr-manager-hero', story: 'fractional-hr-manager-story', process: 'office-informal' },
  'fractional-hr-solutions': { hero: 'office-workspace', story: 'office-open-plan', process: 'office-documents' },
  'temporary-hr-solutions': { hero: 'office-open-plan', story: 'office-collaboration', process: 'office-video-call' },
  'hr-recruitment-netherlands': { hero: 'office-reception', story: 'office-informal', process: 'factory-floor' },
  'interim-hr-advisor': { hero: 'office-video-call', story: 'office-documents', process: 'office-consultation' },
  'interim-hr-support': { hero: 'office-collaboration', story: 'office-workspace', process: 'office-open-plan' },
  'hr-compliance-dutch-entity-foreign-company': { hero: 'office-documents', story: 'office-entrance-amsterdam', process: 'office-workspace' },
  'labor-law-advice-international-employer': { hero: 'office-meeting', story: 'office-video-call', process: 'office-documents' },
};
const fallbackSet = { hero: 'office-consultation', story: 'office-collaboration', process: 'office-documents' };
export const photosFor = (s: string) => photoSets[s] || fallbackSet;
