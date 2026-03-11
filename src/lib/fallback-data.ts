/**
 * Fallback data for when WordPress is not available.
 * This is the current hardcoded content extracted from the Astro pages.
 * Used as a resilience layer — the site builds even without WP.
 */

import type {
    CaseStudy,
    Expertise,
    FAQGroup,
    ResourceHighlight,
    ResourceCaseStudy,
    BlogPost,
} from './wordpress';

// ---------- CASE STUDIES ----------

export const fallbackCaseStudies: CaseStudy[] = [
    {
        slug: 'leadership-training',
        tag: 'Leadership Development',
        title: 'Building Culturally Aware Leaders Across Organisations',
        intro: 'In international and multicultural organisations, leadership effectiveness is deeply shaped by cultural background — yet this dynamic often goes unexamined. We delivered hands-on leadership programmes across multiple client organisations, equipping managers with the insight and tools to lead with greater self-awareness and cultural intelligence.',
        icon: 'school',
        color: 'var(--orange)',
        image: '/images/highlight-leadership.png',
        illustration: '/images/illus-leadership.png',
        items: [
            'Guided participants through structured self-assessments to surface their personal leadership style and its cultural roots',
            'Explored what genuinely drives team performance — and what quietly undermines it — across different cultural contexts',
            'Created space for open dialogue on how culture shapes expectations, communication, and decision-making in teams',
        ],
        outcome: 'Participants left with a sharper understanding of their own style and a practical vocabulary for navigating cultural difference. Organisations saw a measurable shift toward more open, psychologically safe team cultures — where differences are acknowledged, discussed, and turned into a source of strength rather than friction.',
        stats: [],
        floatCards: { tl: { icon: 'groups', label: 'Scope', value: 'Multi-Client' }, br: { icon: 'psychology', label: 'Focus', value: 'Cultural IQ' } },
        context: 'For multiple companies, we delivered hands-on training with a focus on understanding your own style, what works when managing a team, and how culture impacts leadership and style.',
    },
    {
        slug: 'restructuring',
        tag: 'Restructuring & Site Closure',
        title: 'Delivering a Complex Site Closure — On Time and Under Budget',
        intro: 'When a multinational client decided to consolidate operations and close its Dutch site, they faced a tight timeline, regulatory obligations, and the challenge of managing the process with care for the people involved. We were brought in to lead the execution from start to finish.',
        icon: 'domain_disabled',
        color: 'var(--navy)',
        image: '/images/highlight-restructuring.png',
        illustration: '/images/illus-restructuring.png',
        items: [
            'Ensured full legal compliance, including timely and accurate submissions to the Works Council and relevant government authorities',
            'Developed a clear, end-to-end restructuring plan covering stakeholder roles, milestones, and a structured communication strategy',
            'Managed the process with transparency and respect — maintaining trust with employees and management throughout',
        ],
        outcome: 'Despite a last-minute start, the restructuring was completed on schedule and in full compliance with Dutch employment law. The client benefited from a smooth, professionally managed process — and reduced their restructuring costs by 50% compared to initial projections.',
        stats: [
            { value: '50%', label: 'Cost reduction' },
            { value: '100%', label: 'Compliance — zero escalations' },
        ],
        floatCards: { tl: { icon: 'trending_up', label: 'Cost Saving', value: '50%' }, br: { icon: 'verified', label: 'Compliance', value: '100%' } },
        context: 'Client decided to consolidate their activities in one site resulting in closure of the site in NL. We ensured compliance, clear planning, and respectful execution.',
    },
    {
        slug: 'sickness-management',
        tag: 'Absence & Wellbeing Management',
        title: 'Turning Absenteeism from a Cost into a Managed Risk',
        intro: 'High absenteeism is one of the most significant and often underestimated cost drivers in Dutch organisations. For several clients, we introduced structured absence management programmes that combined legal compliance with a genuine culture shift — making sickness a shared responsibility rather than a HR problem.',
        icon: 'health_and_safety',
        color: '#22c55e',
        image: '/images/highlight-sickness.png',
        illustration: '/images/illus-sickness.png',
        items: [
            'Implemented policies and processes fully aligned with the Wet Verbetering Poortwachter (Dutch Gatekeeper Law)',
            'Clarified and embedded accountability across the process — for both managers and employees — through training and clear protocols',
            'Built awareness of the true financial and operational impact of absenteeism at all levels of the organisation',
            'Coached managers on early intervention, supportive conversations, and reintegration best practices',
        ],
        outcome: 'For one client, absenteeism dropped from 7% to 5% — generating annual savings of €500,000 against a total investment of €45,000. That is a return of more than 10×. Across all engagements, clients reported improved manager confidence, faster reintegration, and a more proactive approach to employee wellbeing.',
        stats: [
            { value: '7% → 5%', label: 'Absenteeism reduction' },
            { value: '€500K', label: 'Annual cost saving' },
            { value: '11×', label: 'Return on investment' },
        ],
        floatCards: { tl: { icon: 'savings', label: 'Annual Saving', value: '€500K' }, br: { icon: 'trending_down', label: 'Absence Rate', value: '7%→5%' } },
        context: 'For multiple clients we introduced policies and processes around sickness ensuring compliance, accountability, awareness, and cost reduction.',
    },
];

// ---------- EXPERTISE ----------

export const fallbackExpertise: Expertise[] = [
    {
        slug: 'leadership-training',
        title: 'Leadership Training',
        subtitle: 'Cultural Leadership Development',
        tagline: 'Building self-aware leaders who understand culture\'s impact on success',
        icon: 'school',
        image: '/images/highlight-leadership.png',
        illustration: '/images/illus-leadership.png',
        intro: 'For multiple companies, we deliver hands-on leadership training with a focus on cultural awareness and self-understanding. Our programmes help leaders understand how culture impacts their leadership style and team dynamics.',
        floatCards: { tl: { icon: 'groups', label: 'Reach', value: 'Multi-Client' }, br: { icon: 'psychology', label: 'Focus', value: 'Cultural IQ' } },
        premiseHeading: 'In international organisations, leadership effectiveness is deeply shaped by cultural background — yet this dynamic often goes unexamined.',
        premiseBody: [
            'Standard leadership programmes rarely address the cultural dimension of management. Yet in multicultural organisations, misunderstandings about communication style, decision-making, and expectations are among the most common sources of team friction.',
            'Our leadership training bridges this gap — creating space for honest dialogue, structured self-reflection, and practical tools for leading across cultural boundaries.',
        ],
        included: [
            { title: 'Self-Assessment', desc: 'Structured exercises to surface your personal leadership style and its cultural roots.' },
            { title: 'Team Performance', desc: 'Exploring what genuinely drives team performance — and what quietly undermines it — across different cultural contexts.' },
            { title: 'Open Dialogue', desc: 'Creating space for honest discussion on how culture shapes expectations, communication, and decision-making.' },
            { title: 'Practical Tools', desc: 'Vocabulary and frameworks for navigating cultural difference in day-to-day management.' },
        ],
        result: 'More self-aware leaders who understand how culture impacts their way of working and success. A more open culture where differences can be discussed and appreciated.',
        stats: [],
    },
    {
        slug: 'restructuring',
        title: 'Restructuring',
        subtitle: 'Site Closure & Organizational Change',
        tagline: 'Compliant, respectful restructuring that saves up to 50% on costs',
        icon: 'domain_disabled',
        image: '/images/highlight-restructuring.png',
        illustration: '/images/illus-restructuring.png',
        intro: 'When a client decided to consolidate their activities in one site, resulting in closure of the site in the Netherlands, we helped ensure the process was executed with compliance, clarity, and respect.',
        floatCards: { tl: { icon: 'trending_up', label: 'Cost Saving', value: '50%' }, br: { icon: 'verified', label: 'Compliance', value: '100%' } },
        premiseHeading: 'Restructuring in the Netherlands is governed by strict regulations around Works Councils, government notifications, and employee rights.',
        premiseBody: [
            'Many international companies underestimate the complexity of Dutch restructuring laws. Missing a deadline with the Works Council or failing to properly notify the UWV can lead to costly delays, legal challenges, and reputational damage.',
            'We take the burden off your shoulders — managing the entire process from legal compliance to stakeholder communication, ensuring everything is done right the first time.',
        ],
        included: [
            { title: 'Legal Compliance', desc: 'Ensuring timely and accurate submissions to the Works Council and relevant government authorities.' },
            { title: 'Restructuring Plan', desc: 'Clear, end-to-end plan covering stakeholder roles, milestones, and structured communication strategy.' },
            { title: 'Respectful Execution', desc: 'Managing the process with transparency and respect — maintaining trust with all employees involved.' },
            { title: 'Cost Optimisation', desc: 'Structuring the process to minimize costs while maintaining full legal compliance.' },
        ],
        result: 'The restructuring (although last minute) was executed on time, resulting in a successful process and a cost saving for the client of 50%.',
        stats: [
            { value: '50%', label: 'Cost saving on restructuring' },
            { value: '100%', label: 'On-time delivery' },
        ],
    },
    {
        slug: 'sickness-management',
        title: 'Sickness Management',
        subtitle: 'Absence & Wellbeing Programmes',
        tagline: 'Reducing absenteeism costs — one client saved €500K annually',
        icon: 'health_and_safety',
        image: '/images/highlight-sickness.png',
        illustration: '/images/illus-sickness.png',
        intro: 'For multiple clients we introduced policies and processes around sickness, ensuring compliance with Dutch law while driving accountability and reducing the financial impact of absenteeism.',
        floatCards: { tl: { icon: 'savings', label: 'Annual Saving', value: '€500K' }, br: { icon: 'trending_down', label: 'Absence Rate', value: '7%→5%' } },
        premiseHeading: 'Sickness can be very costly in the Netherlands — employers are obligated to pay 70-100% of salary for up to 2 years of illness.',
        premiseBody: [
            'The Dutch Gatekeeper Law (Wet Verbetering Poortwachter) places strict obligations on both employers and employees during the sickness process. Non-compliance can result in extended salary obligations and UWV sanctions.',
            'Beyond compliance, most organisations lack a proactive approach to absence management. Without clear processes, accountability, and early intervention, absenteeism becomes a silent cost driver that erodes profitability.',
        ],
        included: [
            { title: 'Gatekeeper Compliance', desc: 'Policies and processes fully aligned with the Wet Verbetering Poortwachter (Dutch Gatekeeper Law).' },
            { title: 'Accountability Framework', desc: 'Driving clear accountability for both employees and managers through training and protocols.' },
            { title: 'Cost Awareness', desc: 'Building awareness of the true financial and operational impact of absenteeism at all levels.' },
            { title: 'Manager Coaching', desc: 'Coaching managers on early intervention, supportive conversations, and reintegration best practices.' },
        ],
        result: 'For one client we reduced the sickness rate from 7% to 5%, which resulted in a cost saving of €500,000 with an investment of just €45,000 — a return of more than 10×.',
        stats: [
            { value: '7% → 5%', label: 'Absenteeism reduced' },
            { value: '€500K', label: 'Annual saving' },
            { value: '11×', label: 'Return on investment' },
        ],
    },
];

// ---------- FAQ GROUPS ----------

export const fallbackFAQGroups: FAQGroup[] = [
    {
        category: 'Getting Started',
        items: [
            { q: 'How quickly can you start supporting our company?', a: 'For urgent needs, we arrange an initial consultation within 24 hours. Full project onboarding typically begins within 5 business days, depending on scope.' },
            { q: 'What does a typical engagement look like?', a: 'We offer retainer-based advisory for ongoing support, and fixed-price projects for specific needs like restructuring, compliance audits, or recruitment campaigns. Every engagement starts with a free consultation.' },
            { q: 'Do you support companies outside the Netherlands?', a: 'Yes. While we specialize in Dutch employment law, our network of partners covers the EU and UK for cross-border employment matters, expat onboarding, and 30% ruling applications.' },
        ],
    },
    {
        category: 'Our Services',
        items: [
            { q: 'Are you a traditional HR consultancy?', a: 'No. We are a network organization — a boutique firm that collaborates with specialized partners to deliver best-in-class expertise across every HR discipline, from legal to payroll to talent strategy.' },
            { q: 'Can you help with the 30% ruling for expats?', a: 'Absolutely. We handle the entire application process for the 30% ruling, from evaluating eligibility to submission to the tax authorities (Belastingdienst). We also advise on the recent changes to the ruling.' },
            { q: 'Do you handle payroll administration directly?', a: 'We manage payroll strategy and compliance, and work with specialized payroll ecosystem partners to handle the technical administration and processing. This ensures you get both strategic oversight and operational excellence.' },
        ],
    },
    {
        category: 'Dutch Employment Law',
        items: [
            { q: 'How long does it take to hire an employee in the Netherlands?', a: 'Typically 2-4 weeks for the administrative setup, though this varies based on nationality and visa requirements. For EU citizens, the process is faster. For non-EU citizens requiring a Highly Skilled Migrant visa, allow 4-6 weeks.' },
            { q: 'What are the mandatory employer costs in the Netherlands?', a: 'Beyond gross salary, expect approximately 20-30% additional costs: social insurance contributions (~15-20%), mandatory pension contributions (varies by industry), 8% holiday allowance (vakantiegeld), and sick leave insurance.' },
            { q: 'How does sick leave work under Dutch law?', a: 'Dutch employers must continue paying at least 70% of an employee\'s salary during illness for up to 2 years (104 weeks). You\'re also required to follow the Wet Poortwachter reintegration process and engage an Arbo (occupational health) service.' },
        ],
    },
];

// ---------- RESOURCE HUB PAGE ----------

export const fallbackResourceHighlights: ResourceHighlight[] = [
    {
        title: 'Leadership Training',
        desc: 'Cultural leadership development that builds self-aware, effective leaders across international teams.',
        image: '/images/highlight-leadership.png',
        href: '/resources/expertise/leadership-training',
        icon: 'school',
        stat: 'Multi-client',
    },
    {
        title: 'Restructuring',
        desc: 'Site closure and organizational change executed with compliance, respect, and 50% cost savings.',
        image: '/images/highlight-restructuring.png',
        href: '/resources/expertise/restructuring',
        icon: 'domain_disabled',
        stat: '50% Saved',
    },
    {
        title: 'Sickness Management',
        desc: 'Absence management programmes that reduced absenteeism from 7% to 5%, saving €500K annually.',
        image: '/images/highlight-sickness.png',
        href: '/resources/expertise/sickness-management',
        icon: 'health_and_safety',
        stat: '€500K Saved',
    },
];

export const fallbackResourceCaseStudies: ResourceCaseStudy[] = [
    {
        tag: 'Leadership Development',
        title: 'Building Culturally Aware Leaders',
        desc: 'Hands-on leadership programmes equipping managers with cultural intelligence and self-awareness.',
        icon: 'school',
    },
    {
        tag: 'Restructuring & Site Closure',
        title: 'Complex Site Closure — On Time & Under Budget',
        desc: 'Full restructuring execution with 50% cost reduction and 100% compliance.',
        icon: 'domain_disabled',
    },
    {
        tag: 'Absence & Wellbeing',
        title: 'Turning Absenteeism into a Managed Risk',
        desc: 'Structured absence management generating €500K savings with 11× ROI.',
        icon: 'health_and_safety',
    },
];

// ---------- BLOG POSTS ----------

export const fallbackBlogPosts: BlogPost[] = [
    {
        slug: 'complete-guide-30-percent-ruling-2026',
        title: 'The Complete Guide to 30% Ruling in 2026',
        excerpt: 'Everything international employers and expats need to know about the Dutch 30% ruling — eligibility, recent changes, application process, and practical tips for maximising this valuable tax benefit.',
        content: '<h2>What is the 30% Ruling?</h2><p>The 30% ruling is a Dutch tax advantage for highly skilled migrants recruited from abroad. It allows employers to pay up to 30% of the employee\'s salary as a tax-free allowance, designed to cover the extra costs of living in a foreign country.</p><h2>Key Changes in 2026</h2><p>The Dutch government has implemented significant changes to the 30% ruling. The ruling now follows a step-down structure: 30% for the first 20 months, 20% for months 21-40, and 10% for months 41-60. This applies to new applications from January 2024 onwards.</p><h2>Eligibility Requirements</h2><p>To qualify, the employee must be recruited from abroad (living more than 150km from the Dutch border), possess specific expertise that is scarce in the Netherlands, and meet the minimum salary threshold (€46,107 in 2026, or €35,048 for employees under 30 with a Master\'s degree).</p><h2>Application Process</h2><p>The application is submitted jointly by employer and employee to the Tax Administration (Belastingdienst). Processing typically takes 2-4 months. It\'s crucial to apply within 4 months of the start date to ensure retroactive application.</p>',
        category: 'Guide',
        image: '/images/dutch-business.jpg',
        date: '15 January 2026',
        readTime: '8 min read',
        author: 'HRHelp Team',
    },
    {
        slug: 'dutch-employment-law-employer-guide',
        title: 'Dutch Employment Law: What Every Employer Must Know',
        excerpt: 'A comprehensive overview of Dutch employment law for international employers — from contract types and termination rules to Works Council obligations and the unique aspects of the Dutch labour market.',
        content: '<h2>Understanding Dutch Employment Contracts</h2><p>The Netherlands has a structured system of employment contracts. Fixed-term contracts can be renewed up to three times within a 36-month period, after which they automatically convert to permanent contracts (the "chain rule"). Employers must be aware of the ketenregeling (chain provision) to avoid unintended permanent commitments.</p><h2>Termination and Dismissal</h2><p>Dutch employment law provides strong protections for employees. Dismissal requires either mutual consent, UWV permission (for economic reasons or long-term illness), or court dissolution. The transition payment (transitievergoeding) is mandatory — calculated as one-third of the monthly salary per year of service.</p><h2>Working Hours and Leave</h2><p>Standard working hours are 36-40 per week. Employees are entitled to a minimum of 20 vacation days (based on full-time) plus approximately 8 public holidays. The 8% holiday allowance (vakantiegeld) is paid annually, typically in May.</p><h2>Works Council Requirements</h2><p>Companies with 50+ employees in the Netherlands must establish a Works Council (Ondernemingsraad). This body has advisory and approval rights on key decisions including reorganisations, pension changes, and working conditions policies.</p>',
        category: 'Article',
        image: '/images/professional-woman.jpg',
        date: '28 February 2026',
        readTime: '10 min read',
        author: 'HRHelp Team',
    },
    {
        slug: '5-costly-hr-mistakes-international-companies',
        title: '5 Costly HR Mistakes International Companies Make in NL',
        excerpt: 'International companies expanding to the Netherlands often make expensive HR mistakes. From underestimating sick leave costs to ignoring Works Council obligations — here are the five most costly pitfalls and how to avoid them.',
        content: '<h2>1. Underestimating Sick Leave Obligations</h2><p>In the Netherlands, employers must continue paying at least 70% of salary for up to two years of illness. Many international companies budget for just a few weeks of sick pay, leading to significant unexpected costs. Combined with the Gatekeeper Law obligations, non-compliance can extend this to three years.</p><h2>2. Ignoring the 30% Ruling Deadline</h2><p>The 30% ruling application must be submitted within four months of the employee\'s start date. Missing this deadline means losing the tax benefit entirely — potentially costing thousands of euros per year per employee.</p><h2>3. Mishandling Fixed-Term Contract Renewals</h2><p>The Dutch chain rule (ketenregeling) automatically converts temporary contracts to permanent after three renewals or 36 months. Companies that don\'t track this carefully can find themselves with permanent employees they didn\'t intend to hire long-term.</p><h2>4. Failing to Establish a Works Council</h2><p>Companies with 50 or more employees in the Netherlands are legally required to have a Works Council. Ignoring this obligation can invalidate company decisions and lead to legal challenges from employees.</p><h2>5. Applying Home Country Termination Rules</h2><p>Dutch dismissal law is fundamentally different from most other countries. You cannot simply fire an employee — you need UWV permission, court approval, or a mutual termination agreement. Attempting to apply US or UK-style "at-will" termination leads to costly legal battles and settlements.</p>',
        category: 'Insight',
        image: '/images/remote-worker.jpg',
        date: '5 March 2026',
        readTime: '6 min read',
        author: 'HRHelp Team',
    },
];
