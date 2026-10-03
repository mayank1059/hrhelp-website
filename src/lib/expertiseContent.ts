// Long-form content for the three core expertise pages, kept in the repo as
// src/data/expertise/<slug>.json. WordPress still supplies the title, photo and
// meta; this adds the service-page sections. Returns undefined when a page has
// no JSON yet, so the template falls back to the WordPress-only layout.
// reviewNotes are for the content reviewers and are never rendered.
// Optional fields: seo (title without the brand suffix, meta description, H1;
// otherwise the WordPress title and intro are used), updated (ISO date) and the
// long-form sections; a section without data is left out.

export type ExpertiseContent = {
  slug: string;
  seo?: { title: string; description: string; h1: string };
  updated?: string;
  intro: string;
  situation: { eyebrow: string; heading: string; paragraphs: string[]; keyFacts: { value: string; label: string }[] };
  deepDive?: { eyebrow: string; heading: string; paragraphs: string[]; bullets?: string[] }[];
  timeline?: { eyebrow: string; heading: string; intro: string; rows: { when: string; what: string; who: string }[] };
  approach: { eyebrow: string; heading: string; steps: { title: string; text: string; timing?: string }[] };
  included: { eyebrow: string; heading: string; items: { title: string; text: string }[] };
  helpWith?: {
    eyebrow: string;
    heading: string;
    intro: string;
    solutions: { slug: string; why: string }[];
    services: { slug: string; why: string }[];
  };
  mistakes?: { eyebrow: string; heading: string; items: { title: string; text: string }[] };
  forWho: { eyebrow: string; heading: string; items: string[] };
  pricing: { eyebrow: string; heading: string; text: string };
  glossary?: { eyebrow: string; heading: string; items: { term: string; meaning: string }[] };
  faq: { q: string; a: string }[];
  related: { title: string; href: string; kind: 'guide' | 'blog' | 'solution' | 'service' }[];
  reviewNotes: string[];
};

const files = import.meta.glob<ExpertiseContent>('../data/expertise/*.json', { eager: true, import: 'default' });

export function getExpertiseContent(slug: string): ExpertiseContent | undefined {
  return files[`../data/expertise/${slug}.json`];
}
