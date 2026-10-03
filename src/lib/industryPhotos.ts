// Documentary photos for the industry pages, taken from the service photo set
// (public/images/services-photos/). Replaces the generated sector renders.
// Industrial, life sciences and NGO have their own sector photos
// (public/images/industries-photos/).
import { photo } from './servicePhotos';

const sets: Record<string, { hero: string; spotlight: string; pos?: string }> = {
  technology: { hero: 'office-collaboration', spotlight: 'hr-consultancy-foreign-companies-story' },
  'life-sciences': { hero: 'life-sciences-lab', spotlight: 'interim-hr-manager-story' },
  finance: { hero: 'hr-consultancy-foreign-companies-hero', spotlight: 'office-documents' },
  'professional-services': { hero: 'office-meeting', spotlight: 'office-consultation' },
  logistics: { hero: 'warehouse-floor', spotlight: 'office-workspace' },
  ngo: { hero: 'ngo-office', spotlight: 'fractional-hr-manager-hero' },
  manufacturing: { hero: 'factory-floor', spotlight: 'interim-hr-solutions-hero' },
  industrial: { hero: 'industrial-safety-talk', spotlight: 'office-video-call', pos: '50% 30%' },
};

const own: Record<string, [number, number]> = {
  'industrial-safety-talk': [1000, 1000],
  'life-sciences-lab': [1000, 1000],
  'ngo-office': [1000, 1000],
};
const pick = (n: string, sm: boolean) => {
  if (!own[n]) return photo(n, sm);
  const [w, h] = sm ? [640, Math.round(own[n][1] * 640 / own[n][0])] : own[n];
  return { src: `/images/industries-photos/${n}${sm ? '-sm' : ''}.jpg`, width: w, height: h };
};

export const industryPhotos = (slug: string, sm = false) => {
  const s = sets[slug] || { hero: 'office-open-plan', spotlight: 'office-consultation' };
  return { hero: pick(s.hero, sm), spotlight: pick(s.spotlight, sm), pos: s.pos || '50% 50%' };
};
