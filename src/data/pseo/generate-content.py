#!/usr/bin/env python3
"""Generate HR Teams and HR S.O.S. pSEO JSON data files."""
import json

def make_page(slug, title, subtitle, vertical, vlabel, parent, pname, read, glance, content_h2s, process, pitfalls, faqs, related):
    """Build a page object with HTML content from h2 sections."""
    html = ""
    for h2_title, paragraphs in content_h2s:
        html += f"<h2>{h2_title}</h2>"
        for p in paragraphs:
            if p.startswith("<ul>") or p.startswith("<ol>"):
                html += p
            else:
                html += f"<p>{p}</p>"
    return {
        "slug": slug, "title": title, "subtitle": subtitle,
        "vertical": vertical, "verticalLabel": vlabel,
        "parentService": parent, "parentServiceName": pname,
        "readTime": read,
        "atAGlance": glance, "content": html,
        "process": process, "pitfalls": pitfalls, "faqs": faqs,
        "relatedSlugs": related
    }

# ============================================================
# HR TEAMS — 15 pages
# ============================================================
hr_teams = []

# 1
hr_teams.append(make_page(
    "hr-compliance-checklist-netherlands-2026",
    "HR Compliance Checklist for the Netherlands (2026)",
    "A comprehensive compliance checklist covering all Dutch employment law obligations",
    "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", "12 min read",
    [{"icon":"assignment","label":"Checkpoints","value":"25+"},{"icon":"schedule","label":"Review Cycle","value":"Annual"},{"icon":"gavel","label":"Key Laws","value":"WAB, WNRA, ATW"},{"icon":"euro","label":"Max Penalty","value":"€10,000+"}],
    [("Employment Contract Compliance (2026 Updates)", [
        "Since the implementation of the EU Transparent Terms Directive in August 2022, Dutch employment contracts must contain significantly more mandatory information. All employers should review their standard contracts against 2026 requirements.",
        "<ul><li><strong>Probation clauses:</strong> Must comply with maximum durations per contract type</li><li><strong>Non-compete clauses:</strong> For fixed-term contracts, a written motivation is mandatory</li><li><strong>Training costs:</strong> Mandatory training cannot be charged to employees since August 2022</li><li><strong>Work pattern predictability:</strong> Employees must be informed about predictable work patterns</li></ul>"
    ]),
    ("Leave & Working Hours Requirements", [
        "Dutch working time regulations (Arbeidstijdenwet) set strict limits on daily and weekly working hours, rest periods, and night work. As of 2026, enforcement has increased with the Dutch Labour Authority conducting more inspections.",
        "<ul><li><strong>Maximum hours:</strong> 12 hours per shift, 60 hours per week (average 48 over 16 weeks)</li><li><strong>Rest periods:</strong> Minimum 11 consecutive hours daily, 36 consecutive hours weekly</li><li><strong>Holiday entitlement:</strong> Minimum 4x weekly hours per year (20 days for full-time)</li><li><strong>Sick leave registration:</strong> Employers must register and monitor sick leave from day one</li></ul>"
    ]),
    ("Payroll & Tax Obligations Checklist", [
        "Monthly payroll obligations form the backbone of Dutch employer compliance. Missing deadlines or filing incorrect declarations can trigger automatic penalties.",
        "<ul><li><strong>Loonaangifte:</strong> Monthly wage tax declaration — due by last day of following month</li><li><strong>Vakantiegeld:</strong> 8% holiday allowance — accrued monthly, typically paid in May</li><li><strong>Pension contributions:</strong> Remit to pension fund monthly (if applicable)</li><li><strong>Year-end statements:</strong> Jaaropgave for each employee by February</li></ul>"
    ]),
    ("Health & Safety (ARBO) Compliance", [
        "The Arbeidsomstandighedenwet (ARBO-wet) requires every employer to maintain a safe and healthy working environment. Requirements scale with company size.",
        "<ul><li><strong>RI&E:</strong> Risk Inventory & Evaluation — mandatory for all employers with employees</li><li><strong>Preventiemedewerker:</strong> Every company must designate a prevention officer</li><li><strong>Arbo-dienst contract:</strong> Contract with a certified occupational health service is mandatory</li><li><strong>Workplace inspections:</strong> Regular inspections and incident reporting</li></ul>"
    ]),
    ("Data Protection & Employee Privacy", [
        "The AVG (Dutch implementation of GDPR) imposes strict requirements on how employers handle employee personal data, from recruitment to termination and beyond.",
        "<ul><li><strong>Privacy policy:</strong> Employees must be informed about data processing activities</li><li><strong>Retention periods:</strong> Payroll records 7 years, personnel files 2 years after departure</li><li><strong>Camera surveillance:</strong> Requires works council consent and proportionality assessment</li><li><strong>Email monitoring:</strong> Only permitted under strict conditions with prior notification</li></ul>"
    ])],
    [{"step":"01","title":"Audit Current Contracts & Policies","desc":"Review all employment contracts, handbooks, and HR policies against current Dutch law requirements."},
     {"step":"02","title":"Cross-Reference 2026 Changes","desc":"Check for new legislation effective in 2026 including minimum wage updates, pension reform impacts, and ATW changes."},
     {"step":"03","title":"Implement Updates","desc":"Update contracts, communicate changes to employees, and document all modifications."},
     {"step":"04","title":"Schedule Quarterly Reviews","desc":"Establish a recurring compliance review cycle to catch changes proactively."}],
    [{"severity":"high","title":"Probation Clause Errors","desc":"Invalid probation clauses are void entirely — you cannot terminate an employee during an invalid probation period."},
     {"severity":"high","title":"Non-Compete Without Motivation","desc":"Non-compete clauses in fixed-term contracts without written motivation are automatically void since 2015."},
     {"severity":"medium","title":"CAO Applicability","desc":"If your industry has a generally binding CLA (AVV), it applies regardless of whether you've signed it. Check sector classification."}],
    [{"q":"How often should we review HR compliance?","a":"We recommend quarterly reviews for employment contracts and annually for full compliance audits. Dutch law changes frequently — staying proactive is essential."},
     {"q":"What happens if our contracts are missing mandatory clauses?","a":"Missing mandatory information doesn't void the contract, but exposes the employer to liability claims and may affect the enforceability of other clauses."},
     {"q":"Do we need a works council at 50 employees?","a":"Yes. Once you have 50+ employees in the Netherlands, establishing a works council (ondernemingsraad) is legally mandatory."},
     {"q":"Are there penalties for late loonaangifte filing?","a":"Yes. The Belastingdienst issues automatic penalties starting at €130 per late filing, escalating with repeated offenses."}],
    ["dutch-employment-contracts-guide", "dutch-sick-leave-management", "works-council-requirements-netherlands"]
))

# 2
hr_teams.append(make_page(
    "dutch-employment-contracts-guide",
    "Guide to Dutch Employment Contracts",
    "Everything you need to know about drafting and managing employment contracts in the Netherlands",
    "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", "13 min read",
    [{"icon":"assignment","label":"Contract Types","value":"3 main types"},{"icon":"schedule","label":"Probation Max","value":"2 months"},{"icon":"gavel","label":"Chain Rule","value":"3 contracts / 3 years"},{"icon":"verified","label":"Written Required","value":"Yes (mandatory)"}],
    [("Types of Dutch Employment Contracts", [
        "Dutch law recognizes three main types of employment contracts, each with distinct rules regarding termination, probation periods, and employee protections:",
        "<ul><li><strong>Indefinite contract (onbepaalde tijd):</strong> No end date — the standard for permanent employment. Strongest employee protections. Maximum 2-month probation.</li><li><strong>Fixed-term contract (bepaalde tijd):</strong> Has a specified end date. Maximum 1-month probation for contracts 6mo–2yr. Automatically ends on the end date (no notice needed for contracts ≤6 months).</li><li><strong>On-call contract (oproepovereenkomst):</strong> Zero-hours or min-max contracts. After 12 months, employer must offer fixed hours based on average worked.</li></ul>"
    ]),
    ("Mandatory Contract Clauses (2026)", [
        "Since the implementation of the EU Transparent Terms Directive, Dutch employment contracts must include an extensive list of mandatory information:",
        "<ul><li>Identity and address of both parties</li><li>Place of work or indication of flexibility</li><li>Job title, function description, and grade/level</li><li>Start date (and end date if fixed-term)</li><li>Salary amount, components, and payment frequency</li><li>Working hours and rest period arrangements</li><li>Holiday entitlement and holiday allowance percentage</li><li>Notice period for both parties</li><li>Applicable CLA (if any)</li><li>Pension scheme details</li><li>Training entitlements and policy</li><li>Probation period terms</li></ul>"
    ]),
    ("The Chain Rule (Ketenregeling)", [
        "The chain rule governs when fixed-term contracts automatically convert to indefinite contracts. Understanding this rule is critical for workforce planning:",
        "<ul><li><strong>Maximum 3 consecutive fixed-term contracts:</strong> The 4th contract automatically becomes indefinite</li><li><strong>Maximum 3 years total duration:</strong> If total duration exceeds 3 years, the contract becomes indefinite</li><li><strong>Break period:</strong> A gap of more than 6 months resets the chain completely</li><li><strong>CLA exceptions:</strong> Some CLAs allow up to 6 contracts over 4 years</li></ul>"
    ]),
    ("Probation Period Rules", [
        "Strict rules apply to probation (proeftijd) clauses in Dutch contracts. Invalid probation clauses are completely void — not partially enforceable.",
        "<ul><li>Contracts ≤ 6 months: No probation allowed</li><li>Contracts 6 months – 2 years: Maximum 1 month</li><li>Indefinite or 2+ year contracts: Maximum 2 months</li><li>Must be agreed in writing before the start date</li><li>Must be equal for both employer and employee</li><li>Cannot be included in a renewed contract for the same position</li></ul>"
    ]),
    ("Non-Compete & Confidentiality Clauses", [
        "Dutch courts actively review and restrict non-compete (concurrentiebeding) and relation clauses. Key rules since WAB reform:",
        "<ul><li><strong>Fixed-term contracts:</strong> Non-compete clauses require a written motivation explaining the compelling business interest. Without it, the clause is void.</li><li><strong>Indefinite contracts:</strong> Non-compete is valid without motivation, but courts frequently restrict scope, duration, or geographic reach.</li><li><strong>Compensation:</strong> Former employees may claim compensation if a non-compete unreasonably limits their career options.</li><li><strong>Confidentiality:</strong> NDA clauses are generally enforceable but must be proportionate.</li></ul>"
    ])],
    [{"step":"01","title":"Contract Audit","desc":"Review all existing contracts against current legal requirements and identify gaps."},
     {"step":"02","title":"Template Development","desc":"Create compliant contract templates for each employment type you use."},
     {"step":"03","title":"Clause Optimization","desc":"Draft enforceable non-compete, confidentiality, and IP assignment clauses."},
     {"step":"04","title":"Ongoing Management","desc":"Monitor law changes and update templates annually."}],
    [{"severity":"high","title":"Automatic Indefinite Conversion","desc":"Missing the chain rule limits automatically creates an indefinite contract. This cannot be reversed."},
     {"severity":"high","title":"Void Probation Clauses","desc":"Any probation clause exceeding the legal maximum is entirely void — not reduced to the maximum."},
     {"severity":"medium","title":"Missing Non-Compete Motivation","desc":"Fixed-term contract non-competes without written motivation are automatically void — no cure possible."}],
    [{"q":"Can we use English-language contracts?","a":"Yes. There is no legal requirement for Dutch-language contracts. However, if disputes arise, courts may require certified translations."},
     {"q":"What happens if we forget to include a mandatory clause?","a":"The omission doesn't void the contract, but the employer may be liable for damages if the employee can demonstrate harm from the missing information."},
     {"q":"Can we add a clause after the contract starts?","a":"Amendments to employment contracts require the employee's written consent. Unilateral changes are only possible under very limited circumstances (eenzijdig wijzigingsbeding)."},
     {"q":"Is a digital signature valid?","a":"Yes. Dutch law recognizes electronic signatures for employment contracts, provided they meet the requirements of the eIDAS regulation."}],
    ["hr-compliance-checklist-netherlands-2026", "dutch-sick-leave-management", "dutch-termination-procedures"]
))

# 3
hr_teams.append(make_page(
    "dutch-sick-leave-management",
    "Managing Sick Leave in the Netherlands",
    "How to handle the Dutch 2-year sick leave obligation as an employer",
    "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", "14 min read",
    [{"icon":"healing","label":"Employer Obligation","value":"2 years"},{"icon":"euro","label":"Minimum Pay","value":"70% of salary"},{"icon":"assignment","label":"Key Law","value":"Wet Poortwachter"},{"icon":"gavel","label":"WIA Assessment","value":"After 104 weeks"}],
    [("The Dutch Sick Leave System Explained", [
        "The Netherlands has one of the most extensive employer sick leave obligations in the world. When an employee reports sick, the employer is responsible for continued salary payment and active reintegration for up to 104 weeks (2 years).",
        "This obligation applies from the first day of employment — there is no waiting period. Even an employee who falls ill during their first week triggers the full 2-year obligation."
    ]),
    ("Employer Obligations Under Wet Poortwachter", [
        "The Gatekeeper Improvement Act (Wet verbetering Poortwachter) sets strict procedural requirements for managing long-term sick leave:",
        "<ul><li><strong>Week 1:</strong> Report illness to the Arbo-dienst/company doctor</li><li><strong>Week 6:</strong> Company doctor provides a problem analysis (probleemanalyse)</li><li><strong>Week 8:</strong> Employer and employee create a reintegration plan (Plan van Aanpak)</li><li><strong>Week 42:</strong> Report illness to UWV (the social security agency)</li><li><strong>Every 6 weeks:</strong> Evaluate progress and update the reintegration plan</li><li><strong>Week 52:</strong> Year one evaluation — reassess reintegration strategy</li><li><strong>Week 88:</strong> Employee applies for WIA disability benefit assessment</li><li><strong>Week 104:</strong> End of wage payment obligation (if compliant)</li></ul>"
    ]),
    ("Salary Continuation Requirements", [
        "During illness, employers must continue paying salary according to these rules:",
        "<ul><li><strong>Year 1:</strong> Minimum 70% of salary (many CLAs and contracts require 100%)</li><li><strong>Year 2:</strong> Minimum 70% of salary (often 70% is standard)</li><li><strong>Minimum wage floor:</strong> In Year 1, the payment cannot fall below minimum wage</li><li><strong>Maximum cap:</strong> The payment is capped at the maximum daily wage (maximumdagloon)</li></ul>"
    ]),
    ("Reintegration: First and Second Track", [
        "Employers must actively pursue reintegration of sick employees through two tracks:",
        "<ul><li><strong>First track (spoor 1):</strong> Return to own position or adapted position within the current company. This includes role adjustment, reduced hours, workplace modifications, or reassignment to a different suitable position.</li><li><strong>Second track (spoor 2):</strong> If return to the current employer is not possible, the employer must facilitate reintegration with another employer. This typically involves outplacement services and job coaching.</li></ul>"
    ]),
    ("UWV Sanctions for Non-Compliance", [
        "The UWV audits reintegration efforts when the employee applies for WIA benefits at week 88. If the UWV deems the employer's efforts insufficient, the consequence is severe:",
        "<ul><li><strong>Loonsanctie:</strong> Extended wage payment obligation — the employer must continue paying salary for an additional year (up to 156 weeks total)</li><li><strong>Common failures:</strong> Late problem analysis, insufficient second-track efforts, gaps in documentation, failure to seek expert advice when needed</li></ul>"
    ])],
    [{"step":"01","title":"Illness Reporting","desc":"Employee reports sick — employer notifies Arbo-dienst and begins documentation."},
     {"step":"02","title":"Problem Analysis & Plan","desc":"Company doctor assesses situation; employer and employee create reintegration plan within 8 weeks."},
     {"step":"03","title":"Active Reintegration","desc":"Execute first-track and second-track reintegration with regular evaluations every 6 weeks."},
     {"step":"04","title":"WIA Preparation","desc":"At week 88, support employee's WIA application with complete reintegration dossier."}],
    [{"severity":"high","title":"Loonsanctie Risk","desc":"Insufficient reintegration efforts result in a third year of salary payments — potentially €50,000+ additional cost."},
     {"severity":"high","title":"Dismissal Protection During Illness","desc":"You cannot dismiss a sick employee during the first 2 years of illness (with very narrow exceptions)."},
     {"severity":"medium","title":"Documentation Gaps","desc":"Every step must be documented. Missing documentation is treated as failing to meet obligations."}],
    [{"q":"Can we dismiss an employee who is frequently sick?","a":"Frequent short-term illness can potentially justify dismissal via the court (kantonrechter), but only if it causes unacceptable operational disruption and there is no reasonable accommodation possible."},
     {"q":"What if the employee refuses to cooperate with reintegration?","a":"You can suspend salary continuation after properly warning the employee. However, the threshold is high — document everything and seek legal advice first."},
     {"q":"Do we need sick leave insurance?","a":"It is not mandatory but strongly recommended, especially for smaller companies. Verzuimverzekering covers salary continuation costs and typically includes case management support."},
     {"q":"What happens at the end of 2 years?","a":"If the UWV approves the reintegration efforts, the wage payment obligation ends. The employee either returns to work, receives WIA benefits, or the employment can be terminated via UWV."}],
    ["hr-compliance-checklist-netherlands-2026", "dutch-employment-contracts-guide", "dutch-termination-procedures"]
))

# 4
hr_teams.append(make_page(
    "dutch-termination-procedures",
    "Employee Termination Procedures in the Netherlands",
    "Understanding the three routes to lawful employment termination under Dutch law",
    "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", "13 min read",
    [{"icon":"gavel","label":"Routes","value":"3 legal paths"},{"icon":"euro","label":"Transition Payment","value":"~1/3 month per year"},{"icon":"schedule","label":"Notice Period","value":"1–4 months"},{"icon":"assignment","label":"Grounds Required","value":"8 statutory grounds"}],
    [("The Three Termination Routes", [
        "Dutch law provides three lawful routes to terminate an employment contract. At-will termination does not exist in the Netherlands — every termination requires either mutual agreement or approval from a government body.",
        "<ul><li><strong>Route 1 — Settlement Agreement (vaststellingsovereenkomst):</strong> Mutual termination by agreement. Most common route. Employee has 14-day cooling-off period to revoke.</li><li><strong>Route 2 — UWV Dismissal Permit:</strong> Used for economic dismissal (redundancy) and long-term illness (after 2 years). Processing time 4–6 weeks.</li><li><strong>Route 3 — Court Dissolution (kantonrechter):</strong> Used for performance issues, misconduct, disrupted relationship, and other personal grounds.</li></ul>"
    ]),
    ("The 8 Statutory Grounds for Dismissal", [
        "Since the WAB reform in 2020, Dutch law defines 8 specific grounds for dismissal. Employers can also combine grounds (cumulation) under ground (i):",
        "<ul><li><strong>a) Redundancy:</strong> Economic reasons requiring structural workforce reduction</li><li><strong>b) Long-term illness:</strong> After 2 years of illness with no reintegration prospect</li><li><strong>c) Frequent absence:</strong> Regular short-term illness causing unacceptable operational disruption</li><li><strong>d) Dysfunction:</strong> Inability to perform the role despite coaching and warnings</li><li><strong>e) Culpable conduct:</strong> Serious misconduct (theft, fraud, violence, persistent refusal to work)</li><li><strong>f) Conscientious objection:</strong> Refusal to perform work on moral/religious grounds</li><li><strong>g) Disrupted relationship:</strong> Irreparably damaged working relationship</li><li><strong>h) Other circumstances:</strong> Residual category for situations not covered above</li><li><strong>i) Cumulation:</strong> Combination of two or more incomplete grounds (d, e, g, h) — court may award additional compensation up to 50% of transition payment</li></ul>"
    ]),
    ("Transition Payment Calculation", [
        "Every terminated employee (except summary dismissal for urgent cause) is entitled to a transition payment (transitievergoeding):",
        "<ul><li><strong>Amount:</strong> 1/3 of monthly salary per year of service</li><li><strong>Applies from day 1:</strong> Even during probation period terminations</li><li><strong>Maximum cap:</strong> €94,000 (2026) or one annual salary if higher</li><li><strong>On top of notice period:</strong> The transition payment does not replace the notice period salary</li></ul>"
    ]),
    ("Notice Periods", [
        "Statutory notice periods depend on length of service:",
        "<ul><li>0–5 years: 1 month</li><li>5–10 years: 2 months</li><li>10–15 years: 3 months</li><li>15+ years: 4 months</li><li>Employee notice: always 1 month (unless contract specifies otherwise)</li></ul>"
    ]),
    ("Best Practice: The Settlement Agreement Route", [
        "In practice, 80–90% of Dutch terminations are handled via settlement agreement. This route offers advantages for both parties:",
        "<ul><li>Speed: Can be finalized in days vs. weeks/months for UWV or court routes</li><li>Certainty: Both parties control the outcome</li><li>Reputation: No public court proceedings</li><li>Flexibility: Can include additional arrangements beyond transition payment</li><li>Key requirement: Employee must always have 14 days to revoke the signed agreement</li></ul>"
    ])],
    [{"step":"01","title":"Assess the Situation","desc":"Identify the applicable dismissal ground(s) and determine the best termination route."},
     {"step":"02","title":"Build the Documentation","desc":"Compile performance reviews, warning letters, reintegration files, or business case for redundancy."},
     {"step":"03","title":"Execute the Procedure","desc":"Draft settlement agreement or file UWV/court application with full supporting documentation."},
     {"step":"04","title":"Post-Termination","desc":"Calculate and pay transition payment, issue final salary, and handle administrative closeout."}],
    [{"severity":"high","title":"Missing Performance Documentation","desc":"Dysfunction dismissals require a documented track record of coaching, warnings, and improvement plans. Without it, courts reject the application."},
     {"severity":"high","title":"Forgetting the 14-Day Cooling-Off","desc":"Settlement agreements without the mandatory 14-day revocation period are voidable — the employee can claim the agreement is invalid."},
     {"severity":"medium","title":"Incorrect Transition Payment","desc":"Underpaying the transition payment gives the employee grounds to claim the difference plus interest via the court."}],
    [{"q":"Can we fire someone immediately for misconduct?","a":"Summary dismissal (ontslag op staande voet) is possible for urgent cause, but the threshold is extremely high. The dismissal must happen immediately when the facts become known, and the reason must be unambiguous. Get legal advice before proceeding."},
     {"q":"What if the employee refuses to sign a settlement agreement?","a":"You cannot force a mutual agreement. If the employee declines, you must pursue the UWV or court route. We recommend having a backup plan before entering negotiations."},
     {"q":"Do we owe transition payment if the employee resigns?","a":"No. Transition payment is only owed when the employer initiates termination. Exception: if the employee resigns due to seriously culpable employer conduct."},
     {"q":"How does redundancy selection work?","a":"The 'reflection principle' (afspiegelingsbeginsel) applies — you must select within interchangeable function groups based on age distribution. You cannot cherry-pick."}],
    ["hr-compliance-checklist-netherlands-2026", "dutch-sick-leave-management", "dutch-employment-contracts-guide"]
))

# 5
hr_teams.append(make_page(
    "works-council-requirements-netherlands",
    "Works Council Requirements in the Netherlands",
    "When and how to establish a works council (ondernemingsraad) for your Dutch operations",
    "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", "10 min read",
    [{"icon":"groups","label":"Threshold","value":"50+ employees"},{"icon":"gavel","label":"Key Law","value":"WOR (Wet op de OR)"},{"icon":"verified","label":"Consent Rights","value":"On key HR policies"},{"icon":"schedule","label":"Term","value":"3 years"}],
    [("When Is a Works Council Mandatory?", [
        "Under the Wet op de Ondernemingsraden (WOR), every company operating in the Netherlands with 50 or more employees must establish a works council (ondernemingsraad or OR). This threshold includes all employees regardless of their contract type — full-time, part-time, and fixed-term all count.",
        "Companies with 10–50 employees must establish a personnel representation (personeelsvertegenwoordiging or PVT), which has fewer rights but still requires employer cooperation."
    ]),
    ("Works Council Rights & Powers", [
        "The Dutch works council has three categories of rights:",
        "<ul><li><strong>Consent rights (instemmingsrecht):</strong> The works council must approve changes to working conditions policies, pension schemes, working hours, leave, remuneration systems, health & safety, and performance review systems. Without consent, the employer cannot implement the change.</li><li><strong>Advisory rights (adviesrecht):</strong> The employer must seek the works council's advice on major business decisions: restructuring, mergers, investments, relocations, and significant organizational changes.</li><li><strong>Information rights (informatierecht):</strong> The employer must regularly provide financial results, staffing data, and strategic plans.</li></ul>"
    ]),
    ("Setting Up a Works Council", [
        "The process of establishing a works council involves several formal steps:",
        "<ul><li>Draft a works council regulations (reglement) defining election procedures, seat allocation, and meeting frequency</li><li>Announce elections to all employees and invite candidacies</li><li>Conduct elections by secret ballot</li><li>Install the elected works council members (typically 3–13 members depending on company size)</li><li>Establish a regular meeting cadence (minimum 6 times per year) with the managing director</li></ul>"
    ]),
    ("Common Challenges for International Companies", [
        "International companies often struggle with the works council concept, especially those from countries without similar statutory employee representation. Key challenges include:",
        "<ul><li><strong>Decision-making speed:</strong> Consent and advisory procedures add time to HR policy changes and restructurings</li><li><strong>Scope of influence:</strong> Works councils can block HR policy changes that affect the entire workforce</li><li><strong>Confidentiality:</strong> Works council members receive confidential business information and have a duty of confidentiality</li><li><strong>Training rights:</strong> Works council members are entitled to paid training days (minimum 5 per year)</li></ul>"
    ])],
    [{"step":"01","title":"Threshold Assessment","desc":"Verify employee count and determine whether a full works council or PVT is required."},
     {"step":"02","title":"Regulations & Elections","desc":"Draft works council regulations and organize transparent elections."},
     {"step":"03","title":"Installation & Training","desc":"Install elected members and provide initial training on WOR rights and responsibilities."},
     {"step":"04","title":"Ongoing Collaboration","desc":"Establish productive meeting rhythms and communication protocols between management and OR."}],
    [{"severity":"high","title":"Implementing Without Consent","desc":"HR policy changes implemented without required works council consent can be voided by the court."},
     {"severity":"medium","title":"Ignoring the Advisory Right","desc":"Major decisions made without proper works council advisory can be challenged and potentially reversed."},
     {"severity":"medium","title":"Failing to Establish OR","desc":"Companies that exceed the 50-employee threshold and fail to establish a works council face legal action from employees or unions."}],
    [{"q":"Can we avoid a works council by structuring through multiple entities?","a":"The WOR looks at the economic unit, not just the legal entity. If employees of multiple entities work together as one organization, the threshold applies to the combined workforce."},
     {"q":"Do expat employees count toward the 50-employee threshold?","a":"Yes. All employees with a Dutch employment contract count, regardless of nationality or residency status."},
     {"q":"Can the works council block a restructuring?","a":"The works council has advisory rights on restructurings. If the employer ignores a negative advice, the OR can challenge the decision in court, potentially delaying implementation."},
     {"q":"How much time are works council members entitled to?","a":"Members are entitled to 'sufficient' paid time during working hours for OR activities, plus minimum 5 training days per year. This is additional to their regular leave."}],
    ["hr-compliance-checklist-netherlands-2026", "dutch-employment-contracts-guide", "dutch-termination-procedures"]
))

# 6-15: More HR Teams pages (shorter content)
remaining_teams = [
    ("dutch-holiday-allowance-vakantiegeld", "Dutch Holiday Allowance (Vakantiegeld) Explained", "Understanding the mandatory 8% holiday allowance and how to manage it", "9 min read",
     [{"icon":"euro","label":"Rate","value":"8% of annual salary"},{"icon":"calendar_month","label":"Payout Month","value":"May (typical)"},{"icon":"gavel","label":"Status","value":"Mandatory"},{"icon":"savings","label":"Accrual","value":"Monthly"}]),
    ("dutch-pension-system-employers", "Dutch Pension System for Employers", "Navigating mandatory pension funds, contributions, and compliance obligations", "11 min read",
     [{"icon":"savings","label":"Pillar System","value":"3 pillars"},{"icon":"euro","label":"Employer Cost","value":"10–25% of salary"},{"icon":"gavel","label":"Mandatory Funds","value":"Sector-specific"},{"icon":"schedule","label":"Reform","value":"WTP 2023+"}]),
    ("employee-handbook-netherlands", "Creating an Employee Handbook for the Netherlands", "Essential policies and procedures every Dutch employee handbook should contain", "10 min read",
     [{"icon":"menu_book","label":"Sections","value":"12+ essential"},{"icon":"gavel","label":"Legal Status","value":"Binding if referenced"},{"icon":"groups","label":"OR Consent","value":"Required for key items"},{"icon":"verified","label":"Updates","value":"Annual recommended"}]),
    ("dutch-parental-leave-policies", "Parental Leave Policies in the Netherlands", "WIEG, birth leave, parental leave, and adoption leave obligations for Dutch employers", "10 min read",
     [{"icon":"child_care","label":"Birth Leave","value":"5 days (100% paid)"},{"icon":"schedule","label":"Additional","value":"5 weeks (70% UWV)"},{"icon":"family_restroom","label":"Parental Leave","value":"26 weeks per child"},{"icon":"gavel","label":"Paid Parental","value":"9 weeks at 70% UWV"}]),
    ("dutch-working-time-regulations", "Working Time Regulations in the Netherlands", "Maximum hours, rest periods, overtime rules, and night work compliance under the ATW", "9 min read",
     [{"icon":"schedule","label":"Max Daily","value":"12 hours"},{"icon":"timer","label":"Max Weekly","value":"60 hours (avg 48)"},{"icon":"nightlight","label":"Night Work","value":"Restricted"},{"icon":"pause","label":"Rest Period","value":"11 hours daily"}]),
    ("performance-management-dutch-law", "Performance Management Under Dutch Law", "How to run a legally compliant performance review process that supports potential dismissal cases", "11 min read",
     [{"icon":"trending_up","label":"Reviews","value":"Bi-annual minimum"},{"icon":"assignment","label":"Documentation","value":"Critical"},{"icon":"warning","label":"Improvement Plan","value":"Required before dismissal"},{"icon":"gavel","label":"Court Standard","value":"Documented trajectory"}]),
    ("dutch-remote-work-policy", "Remote Work Policy for the Netherlands", "Creating a compliant thuiswerken policy including the Work Where You Want Act implications", "9 min read",
     [{"icon":"home","label":"Right to Request","value":"Since 2023"},{"icon":"laptop","label":"Equipment","value":"Employer obligation"},{"icon":"euro","label":"WFH Allowance","value":"Tax-free max €2.35/day"},{"icon":"gavel","label":"Key Law","value":"Wet flexibel werken"}]),
    ("restructuring-redundancy-netherlands", "Restructuring & Redundancy in the Netherlands", "How to plan and execute a lawful workforce reduction under Dutch employment law", "12 min read",
     [{"icon":"business","label":"Route","value":"UWV permit required"},{"icon":"groups","label":"Selection","value":"Reflection principle"},{"icon":"euro","label":"Transition Pay","value":"Mandatory"},{"icon":"schedule","label":"Processing","value":"4–6 weeks"}]),
    ("anti-discrimination-dutch-workplace", "Anti-Discrimination in the Dutch Workplace", "Equal treatment obligations, complaints procedures, and employer liability under Dutch law", "10 min read",
     [{"icon":"balance","label":"Key Law","value":"AWGB"},{"icon":"gavel","label":"Protected Grounds","value":"12+ categories"},{"icon":"assignment","label":"Complaints","value":"CRM or internal"},{"icon":"warning","label":"Burden of Proof","value":"Shifts to employer"}]),
    ("expat-employee-management-netherlands", "Managing Expat Employees in the Netherlands", "30% ruling monitoring, BSN registration, and ongoing compliance for international staff", "10 min read",
     [{"icon":"public","label":"30% Ruling","value":"Active monitoring"},{"icon":"assignment","label":"BSN","value":"Required on arrival"},{"icon":"health_and_safety","label":"Insurance","value":"Mandatory ZVW"},{"icon":"school","label":"Integration","value":"Cultural support"}]),
]

for slug, title, subtitle, read, glance in remaining_teams:
    # Generate concise content for remaining pages
    topic = title.split("—")[0] if "—" in title else title
    hr_teams.append(make_page(
        slug, title, subtitle,
        "hr-teams", "HR Teams Guide", "/solutions/hr-teams", "HR Teams", read,
        glance,
        [("Overview", [f"This comprehensive guide covers {subtitle.lower()}. As an employer in the Netherlands, understanding these requirements is essential for compliance and effective workforce management."]),
         ("Key Requirements", [f"<ul><li><strong>Legal framework:</strong> Dutch employment law sets specific requirements for {slug.replace('-', ' ')}</li><li><strong>Employer obligations:</strong> Proactive compliance with all relevant regulations</li><li><strong>Documentation:</strong> All policies and procedures must be documented and communicated</li><li><strong>Regular review:</strong> Annual updates to reflect law changes</li></ul>"]),
         ("Best Practices", ["Working with a specialized Dutch HR partner ensures that your policies are not only legally compliant but also competitive in attracting and retaining talent in the Dutch market."])],
        [{"step":"01","title":"Assessment","desc":"Evaluate current practices against Dutch legal requirements."},
         {"step":"02","title":"Policy Development","desc":"Create or update policies to ensure full compliance."},
         {"step":"03","title":"Implementation","desc":"Roll out updated policies with proper employee communication."},
         {"step":"04","title":"Monitoring","desc":"Ongoing compliance monitoring and annual reviews."}],
        [{"severity":"medium","title":"Non-Compliance Risk","desc":"Failure to comply with Dutch requirements can result in penalties, employee claims, and reputational damage."}],
        [{"q":"Do these requirements apply to all employers?","a":"Yes, all employers with employees in the Netherlands must comply with Dutch employment law, regardless of the parent company's country of origin."},
         {"q":"How often should we review our policies?","a":"We recommend annual reviews, with additional reviews when significant law changes occur."}],
        ["hr-compliance-checklist-netherlands-2026", "dutch-employment-contracts-guide", "dutch-sick-leave-management"]
    ))

# ============================================================
# HR S.O.S. — 15 pages
# ============================================================
hr_sos = []

# 1
hr_sos.append(make_page(
    "dismissing-employee-netherlands-procedure",
    "How to Dismiss an Employee in the Netherlands",
    "Step-by-step guide to lawful employee dismissal under Dutch employment law",
    "hr-sos", "HR S.O.S. Guide", "/solutions/hr-sos", "HR S.O.S.", "14 min read",
    [{"icon":"schedule","label":"Notice Period","value":"1–4 months"},{"icon":"euro","label":"Transition Payment","value":"~1/3 month/year"},{"icon":"assignment","label":"Routes","value":"3 legal paths"},{"icon":"gavel","label":"Grounds Required","value":"8 statutory"}],
    [("Understanding Your Options", [
        "If you need to dismiss an employee in the Netherlands, the first thing to understand is that at-will termination does not exist. Every dismissal must follow one of three legal routes, and every route requires proper documentation and, in most cases, a valid statutory ground.",
        "The route you choose depends on the reason for dismissal, the urgency of the situation, and whether the employee is willing to cooperate."
    ]),
    ("Route 1: Settlement Agreement (Vaststellingsovereenkomst)", [
        "The most common and preferred route — approximately 85% of Dutch terminations use a settlement agreement:",
        "<ul><li><strong>Process:</strong> Employer proposes termination with a package; employee negotiates terms</li><li><strong>Timeline:</strong> Can be completed in days to weeks</li><li><strong>Key terms:</strong> Termination date, severance (at minimum transition payment), notice period compensation, final salary, references, legal cost contribution</li><li><strong>Cooling-off:</strong> Employee has 14 calendar days to revoke a signed agreement — this right cannot be waived</li><li><strong>Unemployment:</strong> If structured correctly, the employee retains the right to unemployment benefits (WW)</li></ul>"
    ]),
    ("Route 2: UWV Dismissal Permit", [
        "Used for two specific grounds: economic dismissal (redundancy) and long-term illness (after 2 years):",
        "<ul><li><strong>Redundancy:</strong> Must demonstrate structural job loss due to financial, organizational, or technological reasons. Reflection principle applies for selection.</li><li><strong>Long-term illness:</strong> Employee must have been sick for 104+ weeks, reintegration must be exhausted, and there must be no prospect of recovery within 26 weeks.</li><li><strong>Processing:</strong> UWV typically decides within 4–6 weeks. Employee can appeal to the court.</li></ul>"
    ]),
    ("Route 3: Court Dissolution (Kantonrechter)", [
        "Used for all other grounds — performance issues, misconduct, disrupted relationships:",
        "<ul><li><strong>Process:</strong> Employer files a petition with the cantonal court. Oral hearing typically within 4–6 weeks.</li><li><strong>Documentation:</strong> The employer must prove the dismissal ground is 'fully substantiated' — partial grounds may justify cumulation (ground i) with additional compensation up to 150% of transition payment.</li><li><strong>Court decision:</strong> The judge can grant or deny dissolution. If granted, sets the termination date and confirms the transition payment amount.</li></ul>"
    ]),
    ("Calculating the Transition Payment", [
        "Every dismissed employee (except summary dismissal for urgent cause) is entitled to a transition payment:",
        "<ul><li><strong>Formula:</strong> 1/3 of gross monthly salary per year of service</li><li><strong>Part years:</strong> Pro-rated for partial years (including months and days)</li><li><strong>Day one:</strong> The right arises from the first day of employment — even probation terminations trigger transition payment</li><li><strong>Maximum:</strong> €94,000 (2026) or one annual salary if higher</li><li><strong>Additional compensation:</strong> Courts can award additional 'fair compensation' (billijke vergoeding) if the employer acted seriously culpably</li></ul>"
    ])],
    [{"step":"01","title":"Assess Situation & Ground","desc":"Identify the applicable dismissal ground and determine the optimal route."},
     {"step":"02","title":"Build Documentation","desc":"Compile all supporting evidence — performance files, financial data, medical reports, warning letters."},
     {"step":"03","title":"Execute Procedure","desc":"Draft settlement proposal, file UWV application, or submit court petition."},
     {"step":"04","title":"Post-Termination","desc":"Process final salary, transition payment, and administrative closeout."}],
    [{"severity":"high","title":"Sick Employee Dismissal Ban","desc":"You cannot dismiss an employee during the first 2 years of illness. Attempting to do so will be reversed by the court."},
     {"severity":"high","title":"Missing 14-Day Cooling-Off Notice","desc":"Settlement agreements must explicitly mention the 14-day revocation right. Without this notice, the cooling-off period extends to 21 days."},
     {"severity":"medium","title":"Inadequate Performance File","desc":"Dysfunction dismissals (ground d) require documented evidence of coaching, warnings, and improvement plans spanning several months."}],
    [{"q":"Can I fire someone immediately for serious misconduct?","a":"Summary dismissal (ontslag op staande voet) is possible but extremely risky. It must happen immediately when the facts are discovered, the reason must be 'urgent cause,' and the employee must be heard first. Courts reverse a significant percentage of summary dismissals."},
     {"q":"How much does a dismissal cost?","a":"At minimum: transition payment (1/3 month per year of service) + notice period salary. In practice, settlement agreements often include 1–3 months additional severance, legal cost contribution (€750–€1,500), and positive reference."},
     {"q":"What if the employee is pregnant?","a":"Pregnant employees have special dismissal protection from the start of pregnancy until 6 weeks after returning from maternity leave. Dismissal during this period is only possible in exceptional circumstances unrelated to the pregnancy."},
     {"q":"Can I reduce the team without individual dismissals?","a":"Not easily. Even in restructuring, each affected employee must receive individual notice, transition payment, and the reflection principle must be applied for selection within interchangeable function groups."}],
    ["emergency-dismissal-netherlands", "settlement-agreement-netherlands", "dutch-employment-law-urgent-questions"]
))

# 2-15: More HR S.O.S. pages
sos_pages = [
    ("emergency-dismissal-netherlands", "Emergency Dismissal (Ontslag op Staande Voet) in the Netherlands", "When and how to execute an immediate dismissal for urgent cause", "11 min read",
     [{"icon":"warning","label":"Timing","value":"Immediate required"},{"icon":"gavel","label":"Risk Level","value":"Very high"},{"icon":"assignment","label":"Documentation","value":"Critical"},{"icon":"euro","label":"Consequence","value":"No transition pay"}]),
    ("settlement-agreement-netherlands", "Drafting a Settlement Agreement (VSO) in the Netherlands", "How to negotiate and structure a legally valid termination agreement", "12 min read",
     [{"icon":"handshake","label":"Usage","value":"~85% of terminations"},{"icon":"schedule","label":"Cooling-Off","value":"14 days"},{"icon":"euro","label":"Minimum","value":"Transition payment"},{"icon":"verified","label":"WW Eligibility","value":"Must be preserved"}]),
    ("dutch-employment-law-urgent-questions", "Dutch Employment Law: Urgent Questions Answered", "Quick answers to the most pressing HR legal questions from international employers", "8 min read",
     [{"icon":"help","label":"Topics","value":"15+ urgent Q&As"},{"icon":"gavel","label":"Focus","value":"Immediate situations"},{"icon":"schedule","label":"Response","value":"Same-day advisory"},{"icon":"verified","label":"Expert","value":"Dutch employment law"}]),
    ("handling-workplace-conflict-netherlands", "Handling Workplace Conflict in the Netherlands", "De-escalation strategies and mediation procedures under Dutch employment law", "10 min read",
     [{"icon":"forum","label":"First Step","value":"Internal mediation"},{"icon":"gavel","label":"Escalation","value":"External mediator"},{"icon":"groups","label":"OR Role","value":"May be involved"},{"icon":"assignment","label":"Documentation","value":"Essential"}]),
    ("employee-fraud-investigation-netherlands", "Employee Fraud Investigation in the Netherlands", "How to investigate suspected fraud while complying with Dutch privacy and employment law", "11 min read",
     [{"icon":"search","label":"Investigation","value":"Privacy-compliant"},{"icon":"gavel","label":"AVG/GDPR","value":"Strict rules apply"},{"icon":"warning","label":"Evidence","value":"Must be lawful"},{"icon":"assignment","label":"Outcome","value":"Summary dismissal possible"}]),
    ("sick-employee-not-cooperating", "When a Sick Employee Doesn't Cooperate", "Legal options when employees refuse reintegration or dispute illness assessments", "10 min read",
     [{"icon":"healing","label":"Obligation","value":"Employee must cooperate"},{"icon":"euro","label":"Sanction","value":"Salary suspension"},{"icon":"gavel","label":"Expert Opinion","value":"Deskundigenoordeel"},{"icon":"warning","label":"Documentation","value":"Critical"}]),
    ("reorganization-crisis-netherlands", "Managing a Reorganization Crisis in the Netherlands", "How to execute an urgent restructuring while complying with Dutch collective dismissal rules", "12 min read",
     [{"icon":"business","label":"WMCO","value":"20+ dismissals"},{"icon":"groups","label":"Union Role","value":"Mandatory consultation"},{"icon":"schedule","label":"Waiting Period","value":"1 month"},{"icon":"euro","label":"Social Plan","value":"Often required"}]),
    ("discrimination-complaint-handling", "Handling a Discrimination Complaint in the Netherlands", "Employer response procedures when facing an internal or external discrimination complaint", "9 min read",
     [{"icon":"balance","label":"Key Law","value":"AWGB"},{"icon":"assignment","label":"Investigation","value":"Required"},{"icon":"gavel","label":"External Body","value":"CRM (College voor de Rechten van de Mens)"},{"icon":"warning","label":"Liability","value":"Employer responsible"}]),
    ("works-council-dispute-resolution", "Resolving Works Council Disputes", "What to do when your works council blocks an important business decision", "10 min read",
     [{"icon":"groups","label":"OR Rights","value":"Consent & Advisory"},{"icon":"gavel","label":"Dispute Body","value":"Enterprise Chamber"},{"icon":"schedule","label":"Timeline","value":"Weeks to months"},{"icon":"handshake","label":"Best Practice","value":"Early engagement"}]),
    ("non-compete-enforcement-netherlands", "Enforcing a Non-Compete Clause in the Netherlands", "How to protect your business interests while navigating strict Dutch judicial scrutiny", "9 min read",
     [{"icon":"shield","label":"Enforceability","value":"Courts often limit"},{"icon":"gavel","label":"Injunction","value":"Kort geding available"},{"icon":"euro","label":"Penalty Clause","value":"Boetebeding"},{"icon":"assignment","label":"Key Factor","value":"Proportionality"}]),
    ("whistleblower-protection-netherlands", "Whistleblower Protection in the Netherlands", "Employer obligations under the Dutch Whistleblower Protection Act (Wet bescherming klokkenluiders)", "10 min read",
     [{"icon":"campaign","label":"Key Law","value":"Wbk (2023)"},{"icon":"groups","label":"Threshold","value":"50+ employees"},{"icon":"assignment","label":"Requirement","value":"Internal reporting channel"},{"icon":"shield","label":"Protection","value":"Retaliation prohibited"}]),
    ("wage-claim-defense-netherlands", "Defending Against Employee Wage Claims", "How to respond when former or current employees claim unpaid wages, overtime, or benefits", "9 min read",
     [{"icon":"euro","label":"Claims","value":"Wages, OT, vacation"},{"icon":"schedule","label":"Limitation","value":"5 years"},{"icon":"gavel","label":"Venue","value":"Kantonrechter"},{"icon":"warning","label":"Statutory Increase","value":"Up to 50%"}]),
    ("data-breach-employee-data-netherlands", "Employee Data Breach Response in the Netherlands", "GDPR/AVG compliance steps when employee personal data is compromised", "9 min read",
     [{"icon":"security","label":"Report Deadline","value":"72 hours to AP"},{"icon":"assignment","label":"Key Law","value":"AVG (GDPR)"},{"icon":"euro","label":"Max Fine","value":"€20M or 4% revenue"},{"icon":"warning","label":"Notification","value":"Employees if high risk"}]),
    ("union-negotiation-crisis", "Navigating a Union Negotiation Crisis", "How to handle CLA negotiations, strikes, and union escalation in the Netherlands", "10 min read",
     [{"icon":"groups","label":"Major Unions","value":"FNV, CNV"},{"icon":"gavel","label":"Strike Right","value":"Protected (conditionally)"},{"icon":"handshake","label":"Mediation","value":"Available"},{"icon":"assignment","label":"CLA","value":"Binding if AVV"}]),
]

for slug, title, subtitle, read, glance in sos_pages:
    hr_sos.append(make_page(
        slug, title, subtitle,
        "hr-sos", "HR S.O.S. Guide", "/solutions/hr-sos", "HR S.O.S.", read,
        glance,
        [("When This Situation Arises", [f"This guide addresses {subtitle.lower()}. In urgent HR situations, having a clear understanding of your legal position and available options is critical."]),
         ("Your Legal Position", [f"<ul><li><strong>Employer obligations:</strong> Dutch law sets specific requirements that must be followed</li><li><strong>Employee rights:</strong> Understand the protections that apply in this situation</li><li><strong>Timeline:</strong> Many situations have strict procedural deadlines</li><li><strong>Documentation:</strong> Every action and communication should be documented</li></ul>"]),
         ("Recommended Actions", ["In crisis HR situations, we strongly recommend engaging specialized Dutch employment law expertise before taking action. Missteps can be costly and often irreversible.", "Contact our HR S.O.S. hotline for immediate guidance on your specific situation."]),
         ("Prevention & Preparation", ["The best way to handle HR crises is to prevent them. Proactive policies, clear documentation practices, and regular compliance reviews significantly reduce the risk of urgent HR situations escalating."])],
        [{"step":"01","title":"Immediate Assessment","desc":"Contact HR S.O.S. for rapid assessment of your legal position and available options."},
         {"step":"02","title":"Strategy Development","desc":"Develop a clear action plan with legal review and risk assessment."},
         {"step":"03","title":"Execution","desc":"Execute the chosen strategy with proper documentation at every step."},
         {"step":"04","title":"Resolution & Prevention","desc":"Resolve the immediate situation and implement preventive measures."}],
        [{"severity":"high","title":"Acting Without Legal Review","desc":"Taking action in urgent HR situations without proper legal review often results in costly reversals and additional liability."},
         {"severity":"medium","title":"Documentation Gaps","desc":"Failing to document actions and communications in real-time weakens your position in any subsequent legal proceedings."}],
        [{"q":"How quickly can I get help?","a":"Our HR S.O.S. service provides same-day initial assessment for urgent situations. Contact us immediately."},
         {"q":"What should I document right now?","a":"Document everything: dates, times, who said what, witnesses present, and any evidence. Keep originals and make copies."},
         {"q":"Can this situation be resolved without going to court?","a":"In most cases, yes. Early intervention and proper handling significantly increase the chances of an out-of-court resolution."}],
        ["dismissing-employee-netherlands-procedure", "dutch-employment-law-urgent-questions", "handling-workplace-conflict-netherlands"]
    ))

# Write files
import os
base = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base, "hr-teams.json"), "w") as f:
    json.dump(hr_teams, f, indent=2, ensure_ascii=False)
    print(f"✅ hr-teams.json — {len(hr_teams)} pages written")

with open(os.path.join(base, "hr-sos.json"), "w") as f:
    json.dump(hr_sos, f, indent=2, ensure_ascii=False)
    print(f"✅ hr-sos.json — {len(hr_sos)} pages written")
