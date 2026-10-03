// Answer options shared by the contact form and the website chatbot, so both
// send identical values to /api/contact (and on to the CRM and WordPress).
export const HELP_NEEDED = [
  '30% ruling & expat onboarding',
  'Sick leave & Wet Poortwachter',
  'Contracts, payroll & compliance',
  'Interim HR / an HR manager',
  'Restructuring or dismissals',
  'Something else',
];

export const EMPLOYEES_NL = ['0 (not hiring yet)', '1–10', '11–50', '51–250', '250+'];

export const TIMELINE = ['This week', 'This month', 'In the next 3 months', 'Just exploring'];

export const PREFERRED_CONTACT = ['Call me', 'Email me', 'Schedule a video call'];

export const QUALITY_IMMIGRATION = (campaign: string) =>
  `https://quality-immigration.com/?utm_source=hrhelp&utm_medium=referral&utm_campaign=${campaign}`;
