// Documentary photos for the resource templates. The resource data (WordPress
// with fallbacks) points at generated renders and flat illustrations; those
// known files are swapped for photos from public/images/services-photos/ when
// rendered. Any other image (for example a real upload in WordPress) is kept.
import { photo } from './servicePhotos';

const swaps: Record<string, string> = {
  '/images/highlight-leadership.png': 'office-video-call',
  '/images/highlight-restructuring.png': 'office-documents',
  '/images/highlight-sickness.png': 'office-consultation',
  '/images/illus-leadership.png': 'office-collaboration',
  '/images/illus-restructuring.png': 'office-meeting',
  '/images/illus-sickness.png': 'interim-hr-manager-story',
};

export const resourcePhoto = (src: string, sm = false) =>
  swaps[src] ? photo(swaps[src], sm) : { src, width: 1200, height: 900 };
