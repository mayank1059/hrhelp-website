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

export const guidePhotos = (index: number) => {
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
