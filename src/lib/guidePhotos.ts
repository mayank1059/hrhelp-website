// Documentary photos for the guide templates (public/images/services-photos/).
// They replace the generated per-guide renders the template used as section
// art (hero, mid-article, key insights and CTA backgrounds). Each guide gets a
// stable, different set of photos from the pool, based on its position.
import { photo } from './servicePhotos';

const pool = [
  'office-consultation', 'office-documents', 'office-collaboration', 'office-meeting',
  'office-video-call', 'office-workspace', 'office-informal', 'office-open-plan',
  'office-reception', 'office-entrance-amsterdam', 'interim-hr-manager-story',
  'hr-consultancy-foreign-companies-hero', 'interim-hr-solutions-hero',
  'fractional-hr-manager-story', 'hr-consultancy-foreign-companies-story',
  'interim-hr-manager-hero', 'fractional-hr-manager-hero',
];

// Guides with their own topic photos (public/images/guide-photos/<slug>-<slot>.jpg),
// keyed by slug, with the alt text for each slot
const ownPhotos: Record<string, Record<'article' | 'insight' | 'inline', string>> = {
  'wet-poortwachter-guide': {
    article: 'HR adviser going through a week-by-week return-to-work plan with an employee',
    insight: 'Occupational physician taking notes while an employee talks about her recovery',
    inline: 'Colleague welcoming an employee back to his desk with a cup of coffee',
  },
  'transition-payment-rules-netherlands': {
    article: 'HR manager and employee discussing a settlement agreement at a meeting table',
    insight: 'Payroll specialist calculating a severance payment from a salary overview',
    inline: 'Employee signing a settlement agreement next to an HR adviser',
  },
  'dutch-maternity-leave': {
    article: 'Pregnant employee going through her handover plan with a colleague',
    insight: 'Pregnant employee working at her desk by the window',
    inline: 'Employee back from maternity leave putting a photo of her baby on her desk as her team lead brings coffee',
  },
  'probation-period-dutch-law': {
    article: 'Team lead helping a new hire set up his laptop on his first day',
    insight: 'Colleague showing a new hire around the office in her first week',
    inline: 'Manager giving a new employee feedback in a probation review',
  },
  'employer-of-record-netherlands': {
    article: 'Dutch team welcoming a new international remote hire on a video call',
    insight: 'Remote employee on a video call with his Dutch team from his home office',
    inline: 'International hire signing her employment contract with an HR adviser',
  },
};

type GuidePhoto = { src: string; width: number; height: number; alt?: string };

export const guidePhotos = (index: number, slug = ''): Record<'article' | 'insight' | 'inline', GuidePhoto> => {
  const own = ownPhotos[slug];
  if (own) {
    const p = (k: 'article' | 'insight' | 'inline', width: number, height: number) =>
      ({ src: `/images/guide-photos/${slug}-${k}.jpg`, width, height, alt: own[k] });
    return { article: p('article', 1600, 800), insight: p('insight', 800, 600), inline: p('inline', 800, 600) };
  }
  const at = (k: number) => pool[(index + k) % pool.length];
  return {
    article: photo(at(4)),
    insight: photo(at(8), true),
    inline: photo(at(12), true),
  };
};

// Topic photos for the guide category cards and vertical heroes
export const verticalPhotos: Record<string, { src: string; width: number; height: number }> = {
  'hr-settlers': { src: '/images/home/solution-settlers.jpg', width: 720, height: 540 },
  'hr-teams': { src: '/images/home/solution-teams.jpg', width: 720, height: 540 },
  'hr-sos': { src: '/images/home/solution-sos.jpg', width: 720, height: 540 },
};
