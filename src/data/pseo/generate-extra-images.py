#!/usr/bin/env python3
"""Generate additional section images for all 46 guide pages using Kie.ai API."""
import requests, time, os, json, sys

API_BASE = "https://api.kie.ai"
API_KEY = "95ed5518f580224ee31b179f803d0685"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
OUTPUT_DIR = "/Users/mayanktewari/Vibe/amsterdamkids/hr/hrhelp-website/public/images/guides"

# For each slug: 4 additional images (content, process, inline, cta)
# Prefixes: content-, process-, inline-, cta-
PAGES = {
    # ===== HR SETTLERS (16) =====
    "starting-business-netherlands-us-company": {
        "content": ("Professional photorealistic image of a Dutch notary office with official documents being signed for company incorporation, elegant wooden interior, brass desk lamp, 4K", "3:2"),
        "process": ("Professional photorealistic image of KvK Chamber of Commerce registration desk in the Netherlands, modern clean government office, digital screens, helpful staff, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a diverse international business team having a strategy meeting in a modern Amsterdam WeWork coworking space, whiteboard with expansion plans, 4K", "16:9"),
        "cta": ("Professional photorealistic image of Amsterdam Zuidas business district at sunset, modern skyscrapers reflecting golden light, professional and aspirational atmosphere, 4K", "16:9"),
    },
    "starting-business-netherlands-uk-company": {
        "content": ("Professional photorealistic image of Brexit customs and trade documents on a desk with EU and UK flags, modern office, serious business planning atmosphere, 4K", "3:2"),
        "process": ("Professional photorealistic image of a video conference between London and Amsterdam offices, dual screens showing both skylines, collaborative remote meeting, 4K", "1:1"),
        "inline": ("Professional photorealistic image of Eurostar terminal at Amsterdam Centraal, business travelers arriving, modern station architecture, international connectivity, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a handshake between two business professionals with Amsterdam canal houses in soft focus background, warm golden light, partnership, 4K", "16:9"),
    },
    "starting-business-netherlands-german-company": {
        "content": ("Professional photorealistic image of German-Dutch bilateral business meeting, engineers reviewing technical plans together, modern meeting room, precision and collaboration, 4K", "3:2"),
        "process": ("Professional photorealistic image of cross-border logistics between Germany and Netherlands, modern highway with trucks, efficient supply chain visualization, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a German executive touring a new Dutch office space in Rotterdam, modern industrial-chic interior, impressed expression, 4K", "16:9"),
        "cta": ("Professional photorealistic image of the Rhine river connecting Germany and Netherlands, cargo ships, bridges, economic partnership symbolism, golden hour, 4K", "16:9"),
    },
    "hiring-first-employee-netherlands": {
        "content": ("Professional photorealistic image of an HR professional drafting an employment contract on a laptop, Dutch employment law book beside them, cozy modern office, focused, 4K", "3:2"),
        "process": ("Professional photorealistic image of a new employee onboarding day in a Dutch office, welcome package on desk with company branded items, bright cheerful atmosphere, 4K", "1:1"),
        "inline": ("Professional photorealistic closeup of a Dutch BSN registration card and DigiD setup on a tablet, official government process, clean organized desk, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a small but growing team celebrating their first hire in a modern Amsterdam startup office, champagne toast, excited team, 4K", "16:9"),
    },
    "netherlands-bv-vs-branch-office": {
        "content": ("Professional photorealistic image of a comparison chart on a whiteboard showing BV vs Branch advantages, modern boardroom, strategic planning session, 4K", "3:2"),
        "process": ("Professional photorealistic image of Dutch corporate legal documents including articles of incorporation for a BV, official stamps, notarial deed, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a modern Dutch BV headquarters with company name on the glass entrance door, professional reception area, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a business advisor presenting entity structure options to international clients, projection screen, modern consulting office, 4K", "16:9"),
    },
    "employer-registration-netherlands": {
        "content": ("Professional photorealistic image of Dutch Belastingdienst tax authority website on a laptop screen showing employer registration form, clean modern office desk, 4K", "3:2"),
        "process": ("Professional photorealistic image of organized filing system with Dutch government correspondence, tax numbers, UWV registration papers, systematic office, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a business owner receiving their KvK registration number confirmation email on laptop, relieved happy expression, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a team of HR consultants helping an international company with Dutch registration paperwork, collaborative office scene, 4K", "16:9"),
    },
    "30-percent-ruling-application-2026": {
        "content": ("Professional photorealistic image of a tax calculation worksheet showing 30 percent ruling salary breakdown, calculator, euro notes, clean financial desk setup, 4K", "3:2"),
        "process": ("Professional photorealistic image of IND immigration application documents for highly skilled migrant, passport, employment contract, organized desk, 4K", "1:1"),
        "inline": ("Professional photorealistic image of an expat family arriving at their new apartment in Amsterdam with moving boxes, excited and optimistic, Dutch neighborhood, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a diverse group of international knowledge workers in a modern Dutch tech company office, multicultural team collaboration, 4K", "16:9"),
    },
    "dutch-payroll-setup-guide": {
        "content": ("Professional photorealistic image of a Dutch payslip (loonstrook) document showing salary components breakdown, vakantiegeld, pension deductions, clean presentation, 4K", "3:2"),
        "process": ("Professional photorealistic image of a payroll specialist setting up automated payroll software on dual monitors, Dutch tax tables visible, organized workspace, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a modern accounting office with organized ledgers, euro currency stacks, financial charts, professional Dutch bookkeeping, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a satisfied business owner reviewing their first successful Dutch payroll run on screen, thumbs up, modern office, 4K", "16:9"),
    },
    "starting-business-netherlands-japanese-company": {
        "content": ("Professional photorealistic image of Japanese and Dutch business cards being exchanged, meishi ritual, formal business etiquette, elegant meeting room, 4K", "3:2"),
        "process": ("Professional photorealistic image of KLM direct flight landing at Schiphol from Tokyo Narita, business class arrival, international connectivity, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a Japanese-Dutch joint venture office with both flags, modern design blending both cultures, respectful workplace, 4K", "16:9"),
        "cta": ("Professional photorealistic image of cherry blossoms in Amsterdam Vondelpark with modern office buildings visible, cultural fusion, spring atmosphere, 4K", "16:9"),
    },
    "starting-business-netherlands-french-company": {
        "content": ("Professional photorealistic image of French-Dutch bilateral trade documents with both flags, modern EU business partnership, legal paperwork, 4K", "3:2"),
        "process": ("Professional photorealistic image of Paris-Amsterdam Thalys business class cabin, executive working on laptop, cross-border commuting lifestyle, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a French patisserie style cafe in Amsterdam functioning as an informal business meeting spot, charming atmosphere, 4K", "16:9"),
        "cta": ("Professional photorealistic image of the Eiffel Tower and Rijksmuseum side by side in a creative composite, French-Dutch business partnership symbolism, 4K", "16:9"),
    },
    "starting-business-netherlands-indian-company": {
        "content": ("Professional photorealistic image of Indian IT professionals collaborating with Dutch colleagues on a software project, modern tech office, agile board visible, 4K", "3:2"),
        "process": ("Professional photorealistic image of visa and work permit documents for Indian nationals, IND office setting, organized immigration paperwork, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a Diwali celebration in a Dutch office with Indian and Dutch employees, cultural integration, festive decorations, 4K", "16:9"),
        "cta": ("Professional photorealistic image of Bangalore and Amsterdam connected by a digital bridge visualization, tech hubs, innovation corridors, modern, 4K", "16:9"),
    },
    "starting-business-netherlands-australian-company": {
        "content": ("Professional photorealistic image of time zone management tools on a screen showing Sydney and Amsterdam clocks, remote collaboration setup, modern office, 4K", "3:2"),
        "process": ("Professional photorealistic image of Australian business documents being apostilled for Dutch use, international legal paperwork, organized professional desk, 4K", "1:1"),
        "inline": ("Professional photorealistic image of casual Australian-style collaborative workspace in Amsterdam, standing desks, open floor plan, relaxed but productive, 4K", "16:9"),
        "cta": ("Professional photorealistic image of Sydney Harbour Bridge at sunrise and Amsterdam at sunset in a creative split composition, global business, 4K", "16:9"),
    },
    "starting-business-netherlands-singapore-company": {
        "content": ("Professional photorealistic image of Singapore-Netherlands double tax treaty documents on a polished conference table, financial planning, both flags visible, 4K", "3:2"),
        "process": ("Professional photorealistic image of Port of Rotterdam container terminal, Asia-Europe trade route, massive cargo ships, global logistics hub, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a Singaporean executive team visiting their new European headquarters in Amsterdam, guided office tour, 4K", "16:9"),
        "cta": ("Professional photorealistic image of Marina Bay Sands and Amsterdam canal houses in a creative dual composition, East meets West business, 4K", "16:9"),
    },
    "starting-business-netherlands-canadian-company": {
        "content": ("Professional photorealistic image of CETA trade agreement documents with Canadian and Dutch flags, modern trade office, international commerce, 4K", "3:2"),
        "process": ("Professional photorealistic image of Dutch company registration completion certificate being printed, official government document, success moment, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a Canadian-Dutch startup team brainstorming with sticky notes on a glass wall, innovative Amsterdam office, 4K", "16:9"),
        "cta": ("Professional photorealistic image of Toronto CN Tower and Amsterdam A'DAM Tower creative composite, Canadian-Dutch business corridor, modern, 4K", "16:9"),
    },
    "work-permits-visa-sponsorship-netherlands": {
        "content": ("Professional photorealistic image of Dutch residence permit card (verblijfsvergunning) and passport on an official desk, immigration documentation, 4K", "3:2"),
        "process": ("Professional photorealistic image of IND recognized sponsor certificate displayed in a modern HR office, authorized employer badge, professional, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a happy international family receiving their Dutch residence permits, celebration outside IND office, 4K", "16:9"),
        "cta": ("Professional photorealistic image of diverse international workforce walking into a modern Dutch company headquarters, welcoming inclusive atmosphere, 4K", "16:9"),
    },
    "business-bank-account-netherlands": {
        "content": ("Professional photorealistic image of Dutch business banking app on a smartphone showing euro transactions, modern fintech interface, clean design, 4K", "3:2"),
        "process": ("Professional photorealistic image of KYC verification documents for Dutch business bank account, passport copies, KvK extract, organized desk, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a modern ING or ABN AMRO business banking center interior, sleek Dutch design, digital screens, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a successful entrepreneur reviewing healthy business financials on a tablet in an Amsterdam cafe, canal view, 4K", "16:9"),
    },
    # ===== HR TEAMS (15) =====
    "hr-compliance-checklist-netherlands-2026": {
        "content": ("Professional photorealistic image of a compliance dashboard on a large screen showing green and red status indicators for HR requirements, modern office, 4K", "3:2"),
        "process": ("Professional photorealistic image of organized HR compliance binders labeled by category, Dutch employment law books, systematic filing, 4K", "1:1"),
        "inline": ("Professional photorealistic image of an HR team conducting a quarterly compliance review meeting, laptops open, checklists on screen, collaborative, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a confident HR director presenting a clean compliance report to the board, green metrics on screen, achievement, 4K", "16:9"),
    },
    "dutch-employment-contracts-guide": {
        "content": ("Professional photorealistic image of a Dutch employment contract being reviewed with a red pen marking key clauses, legal expertise, careful attention, 4K", "3:2"),
        "process": ("Professional photorealistic image of digital contract signing on a tablet with DocuSign interface, modern paperless HR office, 4K", "1:1"),
        "inline": ("Professional photorealistic image of employment law reference books on a shelf with post-it bookmarks, Dutch labor law office, academic atmosphere, 4K", "16:9"),
        "cta": ("Professional photorealistic image of an HR lawyer and business owner shaking hands over finalized contract templates, trust and partnership, 4K", "16:9"),
    },
    "dutch-sick-leave-management": {
        "content": ("Professional photorealistic image of a Wet Poortwachter compliance timeline poster on an HR office wall, clear visual process guide, 4K", "3:2"),
        "process": ("Professional photorealistic image of a company doctor (bedrijfsarts) conducting a professional medical assessment, clinical but caring office, 4K", "1:1"),
        "inline": ("Professional photorealistic image of an employee returning to work after sick leave, warm welcome from colleagues, gradual reintegration, supportive, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a preventive health program poster in a modern Dutch office, ergonomic workstations, wellness focus, 4K", "16:9"),
    },
    "dutch-termination-procedures": {
        "content": ("Professional photorealistic image of UWV dismissal permit application form on a desk with supporting documentation, official procedure, 4K", "3:2"),
        "process": ("Professional photorealistic image of a Dutch kantonrechter courtroom for employment cases, formal judicial setting, empty bench, legal procedure, 4K", "1:1"),
        "inline": ("Professional photorealistic image of transition payment calculation spreadsheet on a monitor, euro amounts, employee service years, precise, 4K", "16:9"),
        "cta": ("Professional photorealistic image of an employment lawyer providing confidential advice to an HR director in a private office, trust, 4K", "16:9"),
    },
    "works-council-requirements-netherlands": {
        "content": ("Professional photorealistic image of works council election ballot box in a Dutch office, democratic process, employee participation, 4K", "3:2"),
        "process": ("Professional photorealistic image of works council members receiving training in a seminar room, WOR rights education, professional development, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a productive OR meeting with management, constructive dialogue, Amsterdam office with canal view, 4K", "16:9"),
        "cta": ("Professional photorealistic image of employee representatives and CEO signing a covenant agreement, partnership and cooperation, 4K", "16:9"),
    },
    "dutch-holiday-allowance-vakantiegeld": {
        "content": ("Professional photorealistic image of May payslip showing vakantiegeld bonus payment highlighted, employee checking bank account, happy revelation, 4K", "3:2"),
        "process": ("Professional photorealistic image of payroll software calculating holiday allowance accrual, spreadsheet with 8% calculations, precise, 4K", "1:1"),
        "inline": ("Professional photorealistic image of Dutch family booking summer holiday at travel agency using vakantiegeld, excited planning, 4K", "16:9"),
        "cta": ("Professional photorealistic image of employees enjoying a summer team outing in the Netherlands, tulip fields in background, happy and relaxed, 4K", "16:9"),
    },
    "dutch-pension-system-employers": {
        "content": ("Professional photorealistic image of three-pillar pension diagram on a presentation screen, financial advisor explaining to business owners, 4K", "3:2"),
        "process": ("Professional photorealistic image of pension fund enrollment forms and employee benefits brochure, organized HR desk, caring employer, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a multigenerational workforce in a Dutch office representing different career stages, pension planning for all ages, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a happy retired couple enjoying Amsterdam canal boat tour, secure retirement, gratitude, golden years, 4K", "16:9"),
    },
    "employee-handbook-netherlands": {
        "content": ("Professional photorealistic image of a modern digital employee handbook on an iPad with clean typography and company branding, interactive table of contents, 4K", "3:2"),
        "process": ("Professional photorealistic image of HR team collaborating on handbook content around a table, post-it notes organizing chapters, creative process, 4K", "1:1"),
        "inline": ("Professional photorealistic image of new employee reading their handbook during orientation week, cozy breakroom with coffee, engaged learning, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a stack of beautifully designed employee handbooks with company logo, professional print quality, modern design, 4K", "16:9"),
    },
    "dutch-parental-leave-policies": {
        "content": ("Professional photorealistic image of parental leave calendar showing WIEG birth leave days highlighted, family photo on desk, planning, 4K", "3:2"),
        "process": ("Professional photorealistic image of UWV parental leave benefit application form on a laptop screen, official government portal, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a father on paternity leave bonding with newborn baby at home, Dutch house interior, tender moment, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a modern Dutch company daycare facility adjacent to the office, children playing, work-life integration, 4K", "16:9"),
    },
    "dutch-working-time-regulations": {
        "content": ("Professional photorealistic image of Arbeidstijdenwet working hours regulation overview chart, clear infographic style on a monitor, 4K", "3:2"),
        "process": ("Professional photorealistic image of a shift planning software interface on a large monitor, color-coded employee schedules, compliance indicators, 4K", "1:1"),
        "inline": ("Professional photorealistic image of Dutch office workers leaving at 5pm sharp, bicycles parked outside, healthy work culture, evening light, 4K", "16:9"),
        "cta": ("Professional photorealistic image of work-life balance scale with briefcase and family, Dutch landscape in background, harmony, 4K", "16:9"),
    },
    "performance-management-dutch-law": {
        "content": ("Professional photorealistic image of a structured performance review form on a tablet, progress ratings, development goals, professional HR tool, 4K", "3:2"),
        "process": ("Professional photorealistic image of a manager coaching session with an employee, whiteboard with growth objectives, collaborative supportive atmosphere, 4K", "1:1"),
        "inline": ("Professional photorealistic image of career development path visualization on a screen, skills matrix, promotions ladder, modern HR analytics, 4K", "16:9"),
        "cta": ("Professional photorealistic image of an employee receiving recognition award, team applauding, positive performance culture in Dutch office, 4K", "16:9"),
    },
    "dutch-remote-work-policy": {
        "content": ("Professional photorealistic image of a thuiswerken policy document on screen with home office setup checklist, modern HR management, 4K", "3:2"),
        "process": ("Professional photorealistic image of ergonomic home office assessment checklist, furniture allowance form, employer compliance with WFH regulations, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a hybrid team meeting with some employees in office and others on video screens, seamless collaboration, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a modern flexible workspace hub in Amsterdam, hot-desking area, collaborative zones, future of work, 4K", "16:9"),
    },
    "restructuring-redundancy-netherlands": {
        "content": ("Professional photorealistic image of reflection principle (afspiegelingsbeginsel) selection matrix on a whiteboard, age groups, function levels, 4K", "3:2"),
        "process": ("Professional photorealistic image of UWV mass layoff notification form being prepared, WMCO compliance, serious administrative process, 4K", "1:1"),
        "inline": ("Professional photorealistic image of outplacement services meeting, career coach helping displaced employee, resume review, supportive transition, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a company emerging stronger after restructuring, new team photo, fresh start, optimistic forward-looking, 4K", "16:9"),
    },
    "anti-discrimination-dutch-workplace": {
        "content": ("Professional photorealistic image of Dutch equal treatment law book AWGB on a desk, rainbow diversity flag pin, inclusive workplace policy documents, 4K", "3:2"),
        "process": ("Professional photorealistic image of diversity and inclusion training workshop in a modern Dutch office, engaged participants, interactive session, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a blind recruitment process on screen, anonymized CVs, fair hiring technology interface, modern HR tech, 4K", "16:9"),
        "cta": ("Professional photorealistic image of International Day of Diversity celebration in a Dutch office, multicultural team, decorations, unity, 4K", "16:9"),
    },
    "expat-employee-management-netherlands": {
        "content": ("Professional photorealistic image of expat relocation package documents including housing allowance letter, international school brochure, welcome guide, 4K", "3:2"),
        "process": ("Professional photorealistic image of BSN registration appointment at Dutch municipality office, expat with appointment letter, official process, 4K", "1:1"),
        "inline": ("Professional photorealistic image of an expat family exploring their new Dutch neighborhood by bicycle, tulips, canal houses, settling in happily, 4K", "16:9"),
        "cta": ("Professional photorealistic image of international team dinner in Amsterdam restaurant, cultural bonding, diverse group celebrating, warm atmosphere, 4K", "16:9"),
    },
    # ===== HR S.O.S. (15) =====
    "dismissing-employee-netherlands-procedure": {
        "content": ("Professional photorealistic image of three dismissal route options diagram on a whiteboard, settlement vs UWV vs court, strategic HR planning, 4K", "3:2"),
        "process": ("Professional photorealistic image of transition payment calculation on a financial calculator with employment records, precise computation, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a confidential HR meeting room with closed door sign, sensitive employee discussion, privacy respected, 4K", "16:9"),
        "cta": ("Professional photorealistic image of HR crisis support hotline team ready to assist, headsets on, multiple screens, responsive service, 4K", "16:9"),
    },
    "emergency-dismissal-netherlands": {
        "content": ("Professional photorealistic image of an incident report document being filed urgently, red URGENT stamp, time-sensitive documentation, 4K", "3:2"),
        "process": ("Professional photorealistic image of legal evidence being organized in a case file, labeled folders, systematic investigation documentation, 4K", "1:1"),
        "inline": ("Professional photorealistic image of an employment crisis meeting with company lawyer present, legal pad with notes, high-stakes discussion, 4K", "16:9"),
        "cta": ("Professional photorealistic image of an emergency legal hotline phone being answered by an employment lawyer, immediate professional response, 4K", "16:9"),
    },
    "settlement-agreement-netherlands": {
        "content": ("Professional photorealistic image of a vaststellingsovereenkomst template document with highlighted key terms, legal review markup, 4K", "3:2"),
        "process": ("Professional photorealistic image of a clock showing 14 days countdown for cooling-off period, calendar with deadline marked, legal timeline, 4K", "1:1"),
        "inline": ("Professional photorealistic image of employee and employer shaking hands after reaching fair settlement, respectful conclusion, professional, 4K", "16:9"),
        "cta": ("Professional photorealistic image of employment mediator facilitating a balanced negotiation, neutral conference room, professional dispute resolution, 4K", "16:9"),
    },
    "dutch-employment-law-urgent-questions": {
        "content": ("Professional photorealistic image of a comprehensive Dutch employment law FAQ guide open on a tablet, searchable index, quick reference, 4K", "3:2"),
        "process": ("Professional photorealistic image of an HR manager speed-dialing their employment law advisor, urgent question, modern phone system, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a legal research session with multiple Dutch law websites open on dual monitors, finding answers fast, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a 24/7 HR legal helpdesk with knowledgeable advisors, always available, professional support team, 4K", "16:9"),
    },
    "handling-workplace-conflict-netherlands": {
        "content": ("Professional photorealistic image of a conflict resolution framework poster on an office wall, escalation steps clearly defined, professional HR tool, 4K", "3:2"),
        "process": ("Professional photorealistic image of a certified mediator MfN setting up a mediation room, neutral space, two chairs, water glasses, 4K", "1:1"),
        "inline": ("Professional photorealistic image of two colleagues reconciling after successful mediation, handshake, relieved expressions, workplace peace, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a team building workshop designed to prevent future conflicts, outdoor activity, Dutch nature, cooperation, 4K", "16:9"),
    },
    "employee-fraud-investigation-netherlands": {
        "content": ("Professional photorealistic image of forensic accounting analysis on dual monitors, suspicious transactions highlighted, digital investigation, 4K", "3:2"),
        "process": ("Professional photorealistic image of a private corporate investigation interview room, recording equipment, legal notepad, controlled environment, 4K", "1:1"),
        "inline": ("Professional photorealistic image of digital forensics tools scanning company data for irregularities, cybersecurity dashboard, investigation, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a fraud prevention training session for employees, compliance presentation, proactive risk management, 4K", "16:9"),
    },
    "sick-employee-not-cooperating": {
        "content": ("Professional photorealistic image of a deskundigenoordeel UWV expert opinion request form on a desk, seeking independent medical assessment, 4K", "3:2"),
        "process": ("Professional photorealistic image of a formal warning letter being drafted regarding reintegration cooperation obligation, serious HR communication, 4K", "1:1"),
        "inline": ("Professional photorealistic image of occupational health specialist reviewing a complex medical case file, concerned professional review, 4K", "16:9"),
        "cta": ("Professional photorealistic image of successful reintegration meeting, employee returning to modified duties, supportive team, positive outcome, 4K", "16:9"),
    },
    "reorganization-crisis-netherlands": {
        "content": ("Professional photorealistic image of a social plan document being drafted for workforce restructuring, union logos visible, negotiation document, 4K", "3:2"),
        "process": ("Professional photorealistic image of WMCO collective dismissal notification being prepared for UWV, official procedure, large scale impact, 4K", "1:1"),
        "inline": ("Professional photorealistic image of trade union representative arriving for CLA negotiation, FNV badge visible, serious business, formal, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a reorganized company team photo, smaller but stronger, new structure, resilient and forward-looking, 4K", "16:9"),
    },
    "discrimination-complaint-handling": {
        "content": ("Professional photorealistic image of a confidential complaint intake form being completed, HR investigation process, respectful and systematic, 4K", "3:2"),
        "process": ("Professional photorealistic image of College voor de Rechten van de Mens building exterior, Dutch human rights tribunal, official and authoritative, 4K", "1:1"),
        "inline": ("Professional photorealistic image of unconscious bias training in progress in a Dutch corporate training room, interactive workshop, awareness, 4K", "16:9"),
        "cta": ("Professional photorealistic image of an inclusive workplace charter being signed by company leadership, commitment to equality, public pledge, 4K", "16:9"),
    },
    "works-council-dispute-resolution": {
        "content": ("Professional photorealistic image of Enterprise Chamber (Ondernemingskamer) court documents for an OR dispute, legal procedure, formal case, 4K", "3:2"),
        "process": ("Professional photorealistic image of a pre-advisory consultation between management and OR, sharing business plans, transparent communication, 4K", "1:1"),
        "inline": ("Professional photorealistic image of works council exercising their consent right, voting on policy change, democratic employee participation, 4K", "16:9"),
        "cta": ("Professional photorealistic image of successful management-OR partnership celebration, collaborative achievement, mutual respect, Dutch workplace, 4K", "16:9"),
    },
    "non-compete-enforcement-netherlands": {
        "content": ("Professional photorealistic image of a non-compete clause being highlighted in yellow in an employment contract, legal review, close examination, 4K", "3:2"),
        "process": ("Professional photorealistic image of kort geding urgent court proceedings preparation, legal briefs being assembled, time-sensitive litigation, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a judge weighing proportionality of non-compete restrictions, scales of justice, employment rights balance, 4K", "16:9"),
        "cta": ("Professional photorealistic image of IP protection security measures in a Dutch tech company, trade secrets management, sophisticated security, 4K", "16:9"),
    },
    "whistleblower-protection-netherlands": {
        "content": ("Professional photorealistic image of a secure digital whistleblower reporting portal on a screen, anonymous submission interface, privacy protection, 4K", "3:2"),
        "process": ("Professional photorealistic image of a whistleblower protection policy document being approved by company board, official implementation, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a compliance officer reviewing a confidential report in a secure office, locked door, discretion, integrity, 4K", "16:9"),
        "cta": ("Professional photorealistic image of ethical company culture poster in an office hallway, speak up culture, integrity values displayed, 4K", "16:9"),
    },
    "wage-claim-defense-netherlands": {
        "content": ("Professional photorealistic image of payroll audit documentation spread on a large desk, years of records, methodical investigation, 4K", "3:2"),
        "process": ("Professional photorealistic image of kantonrechter courtroom benches for a wage claim hearing, employment tribunal setting, Dutch justice, 4K", "1:1"),
        "inline": ("Professional photorealistic image of HR and finance teams collaborating on payroll reconciliation, spreadsheets, cross-referencing, precision, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a modern automated payroll system interface preventing future wage discrepancies, technology solution, 4K", "16:9"),
    },
    "data-breach-employee-data-netherlands": {
        "content": ("Professional photorealistic image of GDPR data breach notification template being filled out within 72-hour deadline, urgent compliance, 4K", "3:2"),
        "process": ("Professional photorealistic image of Autoriteit Persoonsgegevens website on screen showing data breach reporting portal, Dutch DPA, official, 4K", "1:1"),
        "inline": ("Professional photorealistic image of IT security team patching a vulnerability in the employee data system, emergency fix, screens with code, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a modern cybersecurity operations center protecting employee data, monitoring dashboards, secure infrastructure, 4K", "16:9"),
    },
    "union-negotiation-crisis": {
        "content": ("Professional photorealistic image of CLA collective labor agreement document with union and employer signatures section, final draft, 4K", "3:2"),
        "process": ("Professional photorealistic image of FNV union delegates arriving for a negotiation session, carrying briefcases, professional union leadership, 4K", "1:1"),
        "inline": ("Professional photorealistic image of a constructive CLA negotiation breakthrough moment, both parties smiling and relieved, agreement reached, 4K", "16:9"),
        "cta": ("Professional photorealistic image of a harmonious workplace after successful CLA agreement, employees and management satisfied, productive atmosphere, 4K", "16:9"),
    },
}

def create_task(prompt, aspect):
    try:
        r = requests.post(f"{API_BASE}/api/v1/jobs/createTask", headers=HEADERS, json={
            "model": "z-image", "input": {"prompt": prompt, "aspect_ratio": aspect}
        })
        d = r.json()
        data = d.get("data")
        if data and isinstance(data, dict):
            return data.get("taskId")
        return None
    except Exception as e:
        print(f"    ⚠️ API error: {e}")
        return None

def poll_task(task_id, max_wait=180):
    for _ in range(max_wait // 5):
        r = requests.get(f"{API_BASE}/api/v1/jobs/recordInfo?taskId={task_id}", headers=HEADERS)
        d = r.json().get("data", {})
        state = d.get("state", "")
        if state == "success":
            rj = d.get("resultJson", "")
            if rj:
                result = json.loads(rj)
                return result.get("resultUrls", [])
            return []
        elif state in ("failed", "error"):
            return None
        time.sleep(5)
    return None

def download(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, "wb") as f:
            for c in r.iter_content(8192):
                f.write(c)
        return True
    return False

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    existing = set(os.listdir(OUTPUT_DIR))
    image_types = ["content", "process", "inline", "cta"]
    
    start_slug = sys.argv[1] if len(sys.argv) > 1 else None
    started = start_slug is None
    
    slugs = list(PAGES.keys())
    total_images = len(slugs) * 4
    done = 0
    skipped = 0
    
    print(f"\n🎨 Generating {total_images} additional images for {len(slugs)} pages...\n")
    
    for slug in slugs:
        if not started:
            if slug == start_slug:
                started = True
            else:
                continue
        
        page_data = PAGES[slug]
        tasks = {}
        
        for img_type in image_types:
            if img_type not in page_data:
                continue
            fn = f"{img_type}-{slug}.png"
            if fn in existing:
                skipped += 1
                done += 1
                continue
            
            prompt, aspect = page_data[img_type]
            tid = create_task(prompt, aspect)
            if tid:
                tasks[img_type] = tid
            time.sleep(0.3)
        
        if not tasks:
            print(f"  ✅ {slug} — all images exist, skip")
            continue
        
        print(f"  📸 {slug} — submitted {len(tasks)} images")
        
        for img_type, tid in tasks.items():
            urls = poll_task(tid)
            if urls:
                fp = os.path.join(OUTPUT_DIR, f"{img_type}-{slug}.png")
                if download(urls[0], fp):
                    kb = os.path.getsize(fp) // 1024
                    done += 1
                    print(f"    ✅ {img_type}-{slug}.png ({kb} KB)")
                else:
                    print(f"    ❌ Download failed: {img_type}")
            else:
                print(f"    ❌ No result: {img_type}")
        
        time.sleep(0.5)
    
    final = len([f for f in os.listdir(OUTPUT_DIR) if f.endswith(".png")])
    print(f"\n🎉 {final} total images in {OUTPUT_DIR}\n")

if __name__ == "__main__":
    main()
