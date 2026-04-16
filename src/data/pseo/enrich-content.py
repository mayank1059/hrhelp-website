#!/usr/bin/env python3
"""Enrich thin pSEO pages with full-depth content."""
import json, os

BASE = os.path.dirname(__file__)

# Full content for all 24 thin pages
ENRICHMENTS = {
    # ===== HR TEAMS — 10 thin pages =====
    "dutch-holiday-allowance-vakantiegeld": {
        "content": """<h2>What Is Vakantiegeld and Why Does It Matter?</h2>
<p>Vakantiegeld (holiday allowance) is one of the most distinctive features of Dutch employment law. Unlike most countries, the Netherlands legally requires employers to pay an additional <strong>8% of gross annual salary</strong> as holiday allowance. This isn't a bonus — it's a statutory right embedded in the Dutch Civil Code (Article 7:639 BW).</p>
<p>For international companies, understanding vakantiegeld is critical. Failing to calculate or pay it correctly is one of the most common compliance violations that triggers employee claims. The allowance accrues monthly, even during probation periods, sick leave, and notice periods.</p>

<h2>How Is Vakantiegeld Calculated?</h2>
<p>The standard calculation is straightforward: <strong>8% of the employee's gross salary</strong>, including regular wage components. However, several nuances catch employers off guard:</p>
<ul>
<li><strong>Base calculation:</strong> 8% applies to gross salary including fixed allowances and overtime (if structurally agreed)</li>
<li><strong>Variable pay:</strong> Commissions, irregular bonuses, and profit-sharing are typically excluded unless the employment contract or CLA states otherwise</li>
<li><strong>Part-time employees:</strong> Calculated proportionally based on actual hours worked</li>
<li><strong>Accrual period:</strong> Runs from June 1 to May 31 (standard) or follows the calendar year, depending on your payroll setup</li>
</ul>
<p>Some employers negotiate a higher percentage in collective labor agreements (CAOs). In sectors like construction and healthcare, the holiday allowance can exceed 8%. Always check whether a mandatory CLA applies to your industry.</p>

<h2>When and How to Pay Vakantiegeld</h2>
<p>Traditionally, vakantiegeld is paid as a <strong>lump sum in May or June</strong>, coinciding with the start of the summer holiday season. This is when Dutch employees expect to receive their "extra month" of salary.</p>
<p>However, employers can arrange alternative payment schedules:</p>
<ul>
<li><strong>Monthly inclusion:</strong> Some companies include the 8% in monthly gross salary. This must be explicitly stated in the employment contract and clearly visible on payslips</li>
<li><strong>Quarterly payments:</strong> Less common but permissible with employee consent</li>
<li><strong>Upon termination:</strong> Any accrued but unpaid vakantiegeld must be settled in the final paycheck</li>
</ul>
<p>Important: if you include vakantiegeld in monthly salary, you must still show it as a separate line item on the loonstrook (payslip). Bundling it invisibly into the total is not compliant.</p>

<h2>Tax Implications and Payroll Processing</h2>
<p>Vakantiegeld is fully subject to Dutch income tax and social security contributions. The tax treatment depends on how it's paid:</p>
<ul>
<li><strong>Lump-sum payment:</strong> Taxed under the special rate (bijzonder tarief), which can be higher than regular monthly withholding. Employees sometimes feel they "lose" more to tax, though this is reconciled in the annual tax return</li>
<li><strong>Monthly payment:</strong> Taxed as regular income alongside the base salary</li>
<li><strong>Pension contributions:</strong> Vakantiegeld typically counts toward pensionable salary, depending on your pension scheme's definition of "pensioengevend salaris"</li>
</ul>
<p>Your payroll provider should handle these calculations automatically, but it's essential to verify the setup during configuration — especially when transitioning from one payroll system to another.</p>

<h2>Common Mistakes Employers Make</h2>
<p>From our experience supporting hundreds of companies, these are the most frequent vakantiegeld errors:</p>
<ul>
<li><strong>Forgetting to accrue during sick leave:</strong> Employees on sick leave continue to accrue vakantiegeld on the portion of salary they receive (typically 70-100%)</li>
<li><strong>Incorrect base for calculations:</strong> Including or excluding the wrong salary components leads to underpayment claims</li>
<li><strong>Not paying upon termination:</strong> All accrued vakantiegeld must be paid in the final settlement, regardless of the reason for termination</li>
<li><strong>Missing CLA requirements:</strong> Industry-specific CLAs may mandate a higher percentage or different payment schedule</li>
</ul>"""
    },
    "dutch-pension-system-employers": {
        "content": """<h2>Understanding the Dutch Three-Pillar Pension System</h2>
<p>The Netherlands operates one of the world's most robust pension systems, consistently ranked in the top 3 globally by the Mercer Global Pension Index. For employers, understanding this system is crucial because <strong>pension obligations are a significant cost of employment</strong> — typically adding 15-25% on top of gross salary costs.</p>
<p>The system is built on three pillars:</p>
<ul>
<li><strong>Pillar 1 — AOW (State Pension):</strong> Universal basic retirement income funded through taxes. Every resident builds up 2% per year of residency (50 years for full entitlement). The current AOW age is 67 years and 3 months</li>
<li><strong>Pillar 2 — Occupational Pension:</strong> Employer-facilitated pension through industry or company pension funds. This is where most employer obligations lie</li>
<li><strong>Pillar 3 — Individual Savings:</strong> Personal retirement savings and investments. Not an employer responsibility</li>
</ul>

<h2>Mandatory vs. Voluntary Pension Enrollment</h2>
<p>One of the most critical questions for employers: do you <em>have</em> to offer a pension? The answer depends on your situation:</p>
<ul>
<li><strong>Mandatory industry pension fund (BPF):</strong> If your company falls under a sector with a mandatory pension fund (e.g., PFZW for healthcare, ABP for government, PME for metals), you <em>must</em> enroll all eligible employees. Non-compliance results in backdated contributions plus penalties</li>
<li><strong>CLA-mandated pension:</strong> Some collective labor agreements require pension participation even without a BPF</li>
<li><strong>Voluntary company pension:</strong> If no mandatory scheme applies, offering a pension is technically optional — but expected. Most Dutch employees consider pension a standard benefit, and not offering one creates a serious competitive disadvantage in recruitment</li>
</ul>
<p>The <strong>Wet toekomst pensioenen (WTP)</strong> — the Future of Pensions Act — which took effect January 1, 2024, is fundamentally restructuring pillar 2 pensions. All existing defined benefit (DB) schemes must transition to defined contribution (DC) schemes by January 1, 2028. Every employer with a pension scheme needs a transition plan.</p>

<h2>Managing Pension Costs and Administration</h2>
<p>Pension is typically the second-largest employment cost after gross salary. Key cost considerations:</p>
<ul>
<li><strong>Contribution split:</strong> Usually shared between employer (⅔) and employee (⅓), though this varies by scheme and agreement</li>
<li><strong>Pensionable salary base:</strong> Defined as gross salary minus the AOW franchise (the portion covered by state pension). The franchise amount is set annually</li>
<li><strong>Maximum pensionable salary:</strong> Currently capped at approximately €130,000 (fiscally allowable limit)</li>
<li><strong>Administration:</strong> Pension fund reporting, premium calculations, and employee communications require dedicated processes</li>
</ul>

<h2>International Employee Considerations</h2>
<p>For international companies, pension adds complexity for globally mobile employees:</p>
<ul>
<li><strong>30% ruling holders:</strong> Can opt out of Dutch social security (including AOW accrual) if they maintain home-country coverage. This doesn't automatically exempt them from pillar 2 pension</li>
<li><strong>Posted workers:</strong> May remain in their home-country pension system under EU social security coordination rules (A1 certificate)</li>
<li><strong>Short-term assignments:</strong> Consider whether enrollment in the Dutch pension scheme is required or sensible for employees on limited-duration contracts</li>
</ul>"""
    },
    "employee-handbook-netherlands": {
        "content": """<h2>Why Every Company in the Netherlands Needs an Employee Handbook</h2>
<p>An employee handbook (personeelshandboek) is more than an HR document — it's a <strong>legal shield and cultural foundation</strong> for your Netherlands operations. While not strictly required by Dutch law, having a comprehensive handbook is considered best practice and provides critical legal protection.</p>
<p>In Dutch employment law, employer policies documented in a handbook can be legally binding — but only if properly communicated and acknowledged. A well-crafted handbook sets clear expectations, reduces workplace disputes, and demonstrates compliance during labor inspections or court proceedings.</p>

<h2>Essential Sections for Dutch Compliance</h2>
<p>Your handbook must address several Dutch-specific requirements that may not exist in your home country:</p>
<ul>
<li><strong>Working hours and Arbeidstijdenwet compliance:</strong> Maximum daily/weekly hours, rest periods, overtime policies, and right to request schedule changes</li>
<li><strong>Leave entitlements:</strong> Statutory vacation days (4× weekly hours), bovenwettelijk (extra-statutory) days, sick leave procedures, parental leave, calamity leave, and special leave categories</li>
<li><strong>Sick leave and reintegration:</strong> Wet Poortwachter obligations, reporting procedures, company doctor (bedrijfsarts) visits, and reintegration expectations</li>
<li><strong>Remote work policy:</strong> Following the Wet flexibel werken, employees can request home working. Your policy should address equipment, expenses, and availability</li>
<li><strong>Anti-discrimination and complaints:</strong> Confidential advisor (vertrouwenspersoon) procedures, complaint mechanisms, and anti-harassment policies</li>
<li><strong>Privacy and data protection:</strong> GDPR/AVG requirements for employee data processing, monitoring policies, and consent procedures</li>
</ul>

<h2>Legal Enforceability: What Makes It Binding?</h2>
<p>Under Dutch law, a handbook becomes legally binding through several mechanisms:</p>
<ul>
<li><strong>Incorporation by reference:</strong> The employment contract explicitly refers to the handbook and the employee acknowledges receipt</li>
<li><strong>Reasonable policies:</strong> Courts assess whether policies are reasonable and balanced — unreasonable restrictions may be struck down</li>
<li><strong>Works council consent:</strong> If you have a works council (OR), several handbook policies require their consent under Article 27 WOR (e.g., working hours, leave, safety, privacy)</li>
<li><strong>Unilateral changes:</strong> You cannot simply update the handbook and impose new conditions. Article 7:613 BW requires a "zwaarwichtig belang" (compelling interest) for unilateral changes</li>
</ul>

<h2>Creating a Handbook That Works for International Teams</h2>
<p>For international companies, the handbook serves a dual purpose: ensuring Dutch compliance and bridging cultural expectations. Consider these best practices:</p>
<ul>
<li><strong>Language:</strong> Provide the handbook in English (for international staff) and Dutch (for legal certainty). In case of conflict, specify which version prevails</li>
<li><strong>Global vs. local policies:</strong> Clearly distinguish between global company policies and Netherlands-specific regulations. Dutch law always takes precedence</li>
<li><strong>Tone and style:</strong> The Dutch work culture values directness and transparency. Avoid corporate jargon — be clear, practical, and straightforward</li>
<li><strong>Regular updates:</strong> Dutch employment law changes frequently. Review your handbook annually, especially after legislative changes (e.g., WTP pension reform, Wet werken waar je wilt)</li>
</ul>"""
    },
    "dutch-parental-leave-policies": {
        "content": """<h2>Overview of Dutch Parental Leave Rights</h2>
<p>The Netherlands offers one of Europe's most comprehensive parental leave frameworks, with <strong>multiple types of leave</strong> available to new parents. Understanding these entitlements is essential for employers — particularly because recent legislation has significantly expanded employee rights.</p>
<p>Dutch parental leave consists of several distinct types, each with different duration, payment levels, and eligibility criteria. Getting these wrong exposes you to employee claims and potential UWV penalties.</p>

<h2>Types of Leave for New Parents</h2>
<p>Here's a complete breakdown of every leave type available:</p>
<ul>
<li><strong>Zwangerschapsverlof (Pregnancy leave):</strong> 6 weeks before the due date (can start 4 weeks before). Paid at 100% by UWV through the WAZO</li>
<li><strong>Bevallingsverlof (Maternity leave):</strong> Minimum 10 weeks after birth. Combined with pregnancy leave, the total is always at least 16 weeks. Paid at 100% by UWV</li>
<li><strong>Geboorteverlof (Birth leave — partners):</strong> 1 week at 100% salary, paid by employer. Must be taken within 4 weeks of birth</li>
<li><strong>Aanvullend geboorteverlof (Additional birth leave):</strong> 5 additional weeks within 6 months of birth. Paid at 70% of daily wage by UWV (capped at maximum daily wage)</li>
<li><strong>Ouderschapsverlof (Parental leave):</strong> 26 weeks per parent, per child, until the child turns 8. The first 9 weeks are paid at 70% by UWV (if taken in the child's first year). Remaining 17 weeks are unpaid</li>
</ul>

<h2>Employer Obligations and Administration</h2>
<p>Managing parental leave requires careful HR administration:</p>
<ul>
<li><strong>Cannot refuse:</strong> Employers must honor all statutory leave requests. You can discuss timing and scheduling, but cannot deny the leave itself</li>
<li><strong>Continued benefit accrual:</strong> Holiday allowance (vakantiegeld), pension contributions, and vacation days continue to accrue during paid leave</li>
<li><strong>UWV applications:</strong> Birth mothers and partners must apply to UWV for benefits. Employers facilitate by providing required employment data</li>
<li><strong>Return-to-work:</strong> Employees have the right to return to their same position (or equivalent) after leave. You cannot restructure someone's role while they're on parental leave</li>
<li><strong>Flexible arrangements:</strong> Many parents request adjusted working hours upon return. Under the Wet flexibel werken, you can only refuse with compelling business reasons</li>
</ul>

<h2>Strategic Considerations for Employers</h2>
<p>Beyond compliance, smart employers use parental leave policies to attract and retain top talent:</p>
<ul>
<li><strong>Top-up policies:</strong> Many competitive employers supplement UWV payments to 100% salary during additional birth leave and the paid parental leave period</li>
<li><strong>Extended unpaid leave:</strong> Offering longer leave (beyond statutory) is a powerful retention tool, especially for senior employees</li>
<li><strong>Phased return:</strong> Supporting gradual return-to-work schedules (e.g., starting at 60% hours) reduces turnover and improves employee wellbeing</li>
<li><strong>Documentation:</strong> Keep detailed records of leave requests, dates, and UWV correspondence. Disputes about leave duration or pay can arise years later</li>
</ul>"""
    },
    "dutch-working-time-regulations": {
        "content": """<h2>The Arbeidstijdenwet: Core Rules for Employers</h2>
<p>The Dutch Working Hours Act (Arbeidstijdenwet, or ATW) sets strict limits on when and how long employees can work. For international companies used to more flexible labor markets, these regulations can feel restrictive — but compliance is non-negotiable and strictly enforced by the Dutch Labour Inspectorate (Arbeidsinspectie).</p>
<p>The key limits every employer must know:</p>
<ul>
<li><strong>Maximum per shift:</strong> 12 hours per day</li>
<li><strong>Maximum per week:</strong> 60 hours in any single week</li>
<li><strong>Average maximum:</strong> 48 hours per week averaged over 16 weeks</li>
<li><strong>Annual maximum:</strong> No more than 2,304 hours per year for full-time employees</li>
</ul>

<h2>Rest Periods and Break Requirements</h2>
<p>Equally important are the mandatory rest periods — these cannot be waived, even with employee consent:</p>
<ul>
<li><strong>Daily rest:</strong> Minimum 11 consecutive hours between shifts. Can be reduced to 8 hours once per 7-day period in exceptional circumstances</li>
<li><strong>Weekly rest:</strong> 36 consecutive hours of rest per 7 days, or 72 hours per 14 days (which can be split into blocks of at least 32 hours)</li>
<li><strong>Breaks:</strong> After 5.5 hours of work: minimum 30 minutes (can be split into 2×15 minutes). After 10 hours: minimum 45 minutes total</li>
</ul>
<p>These minimums apply to all employees. Collective labor agreements (CAOs) may set stricter requirements for specific sectors.</p>

<h2>Night Work and On-Call Regulations</h2>
<p>Night work (between 00:00 and 06:00) carries additional restrictions:</p>
<ul>
<li><strong>Maximum night shifts:</strong> 10 hours per shift, 40 hours per week</li>
<li><strong>Frequency limits:</strong> Maximum 36 night shifts in 16 weeks, or 140 night shifts per year</li>
<li><strong>Health checks:</strong> Employers must offer periodic health assessments to night workers</li>
<li><strong>On-call duty (bereikbaarheidsdienst):</strong> Time spent on-call at home counts differently from time at the workplace. Active on-call time at the employer's premises counts as regular working hours</li>
</ul>

<h2>Right to Request Working Hours Changes</h2>
<p>Under the <strong>Wet flexibel werken</strong> (Flexible Working Act), employees who have been employed for 26+ weeks can request changes to:</p>
<ul>
<li>Total working hours (more or fewer)</li>
<li>Schedule/distribution of hours across the week</li>
<li>Place of work (including working from home)</li>
</ul>
<p>Employers can only refuse these requests if there are <strong>compelling business interests</strong> (zwaarwegend bedrijfsbelang). Simply preferring the current arrangement is not sufficient grounds for refusal.</p>

<h2>Enforcement and Penalties</h2>
<p>The Dutch Labour Inspectorate conducts both random and targeted inspections. Violations can result in:</p>
<ul>
<li>Administrative fines up to <strong>€10,000 per violation</strong></li>
<li>Criminal prosecution for repeated or serious violations</li>
<li>Requirement to implement a remediation plan</li>
<li>Reputational damage and employee trust erosion</li>
</ul>
<p>Maintaining proper time registration is essential proof of compliance. Digital timekeeping systems are strongly recommended.</p>"""
    },
    "performance-management-dutch-law": {
        "content": """<h2>Performance Management in the Dutch Legal Context</h2>
<p>Performance management in the Netherlands operates within a fundamentally different legal framework than in many other countries. The Dutch principle of <strong>"goed werknemerschap" and "goed werkgeverschap"</strong> (good employee and good employer conduct) means that managing underperformance requires a structured, documented, and supportive approach.</p>
<p>You cannot simply terminate an employee for poor performance. Dutch courts (and UWV) require evidence that you followed a <strong>fair and reasonable improvement process</strong> before any dismissal for underperformance (disfunctioneren) can be considered.</p>

<h2>Building a Legally Sound Performance Framework</h2>
<p>A compliant performance management system should include:</p>
<ul>
<li><strong>Clear function profiles:</strong> Written role descriptions with measurable objectives and key competencies. Without these baseline expectations, proving underperformance is nearly impossible</li>
<li><strong>Regular evaluations:</strong> At minimum, annual performance reviews with documented outcomes. Biannual or quarterly reviews are recommended</li>
<li><strong>Two-way dialogue:</strong> Dutch employment law values the employee's input. Evaluations should be discussions, not one-sided assessments</li>
<li><strong>Written records:</strong> Every performance conversation should be documented with a signed summary. Email confirmations of discussions provide crucial evidence if disputes arise</li>
</ul>

<h2>The Performance Improvement Plan (Verbetertraject)</h2>
<p>When an employee underperforms, Dutch law requires a formal improvement trajectory before any termination can be pursued:</p>
<ul>
<li><strong>Clear notification:</strong> The employee must be explicitly told that their performance is insufficient, with specific examples and measurable criteria</li>
<li><strong>Adequate support:</strong> You must provide coaching, training, mentoring, or other support to help the employee improve. Simply identifying problems without offering solutions fails the "goed werkgeverschap" test</li>
<li><strong>Reasonable timeframe:</strong> The improvement period must be proportional — typically 3 to 6 months depending on the role and nature of the issues</li>
<li><strong>Regular check-ins:</strong> Progress meetings (at least monthly) with documented feedback on improvement or continued shortcomings</li>
<li><strong>Alternative positions:</strong> Before termination, you must genuinely explore whether the employee can be placed in a different suitable role within the organization</li>
</ul>

<h2>Common Pitfalls That Undermine Dismissal Cases</h2>
<p>Courts regularly reject dismissal requests due to employer failures in the improvement process:</p>
<ul>
<li><strong>"Sudden" underperformance:</strong> If previous reviews were positive or neutral, claiming sudden poor performance lacks credibility. Build a consistent track record</li>
<li><strong>vague feedback:</strong> "Not a team player" or "lacks initiative" without specific, documented examples will not satisfy a court</li>
<li><strong>Insufficient support:</strong> Employers who say "we expected self-improvement" without providing concrete tools and training will lose their case</li>
<li><strong>Unrealistic timelines:</strong> A 4-week improvement plan for complex behavioral issues signals that the employer wasn't genuinely committed to improvement</li>
</ul>"""
    },
    "dutch-remote-work-policy": {
        "content": """<h2>Remote Work Rights in the Netherlands</h2>
<p>Remote working (thuiswerken) has become deeply embedded in Dutch work culture, accelerated by the pandemic but now formalized in legislation. The <strong>Wet werken waar je wilt</strong> (Work Where You Want Act) strengthened employee rights to request remote working, and employers need robust policies to manage this effectively.</p>
<p>Under current Dutch law, employees of companies with 10+ workers can submit a formal request to change their place of work — including working from home. Employers must seriously consider these requests and can only refuse on reasonable business grounds. A blanket "no remote working" policy is increasingly difficult to defend.</p>

<h2>Employer Obligations for Home Workers</h2>
<p>When employees work from home, your duty of care (zorgplicht) doesn't stop at the office door:</p>
<ul>
<li><strong>Ergonomic workspace:</strong> Under the Arbeidsomstandighedenwet (Working Conditions Act), employers must ensure home workstations meet ergonomic standards. This typically means providing or subsidizing a proper desk, chair, and monitor</li>
<li><strong>Equipment and connectivity:</strong> Provide necessary work equipment (laptop, keyboard, headset) and consider contributing to internet costs</li>
<li><strong>Home working allowance:</strong> Many employers provide a tax-free allowance of up to €2.35 per home working day (2024 rate) for utilities and supplies</li>
<li><strong>Workplace assessment:</strong> Technically, you should assess the home workspace (or have the employee complete a self-assessment checklist). Document this for Arbeidsinspectie compliance</li>
</ul>

<h2>Managing Hybrid Teams Effectively</h2>
<p>The practical challenge isn't legal compliance — it's making hybrid work actually work:</p>
<ul>
<li><strong>Clear expectations:</strong> Define core office days (if any), availability hours, and communication norms. Ambiguity breeds frustration on both sides</li>
<li><strong>Equal treatment:</strong> Avoid creating a "two-tier" workforce where office-based employees receive more visibility and career opportunities</li>
<li><strong>Results-oriented management:</strong> Dutch work culture already favors output over presence. Reinforce this by measuring deliverables, not hours online</li>
<li><strong>Social connection:</strong> Schedule regular in-person team moments. Dutch employees value "gezelligheid" (conviviality) and team bonding</li>
</ul>

<h2>Cross-Border Remote Work Complications</h2>
<p>For international companies, remote work introduces complex issues:</p>
<ul>
<li><strong>Tax implications:</strong> Employees working from another country for extended periods may trigger a permanent establishment (vaste inrichting) or personal tax obligations in that country</li>
<li><strong>Social security:</strong> Under EU rules, employees working 25%+ of their time in their country of residence may shift social security obligations to that country</li>
<li><strong>30% ruling risk:</strong> Excessive work outside the Netherlands can jeopardize an employee's 30% ruling eligibility</li>
<li><strong>Employment law:</strong> Extended work from another country may trigger that country's mandatory employment protections</li>
</ul>
<p>We recommend capping international remote work at 10-15 days per year unless you've obtained specific tax and social security advice.</p>"""
    },
    "restructuring-redundancy-netherlands": {
        "content": """<h2>Restructuring Under Dutch Employment Law</h2>
<p>Reorganization in the Netherlands is one of the most heavily regulated employment processes internationally. Unlike many countries where at-will employment allows rapid workforce reductions, Dutch law requires employers to follow <strong>strict substantive and procedural requirements</strong>. Getting these wrong means denied dismissal permits, costly court challenges, and reputational damage.</p>
<p>The legal basis for restructuring dismissals falls under the "bedrijfseconomische redenen" (business-economic reasons) ground, which includes financial necessity, organizational changes, technological automation, or business closure.</p>

<h2>The UWV Route: Collective Dismissal Procedures</h2>
<p>For economic dismissals, employers must obtain permission from UWV (the Dutch Employee Insurance Agency). The process involves:</p>
<ul>
<li><strong>Business case documentation:</strong> You must demonstrate with financial evidence why the restructuring is necessary. UWV scrutinizes business plans, financial statements, and market analyses</li>
<li><strong>Function elimination:</strong> Show which specific functions are being eliminated or modified, and why. Vague claims about "efficiency" are insufficient</li>
<li><strong>Afspiegelingsbeginsel (Reflection Principle):</strong> When selecting which employees to dismiss within a function group, you must apply a legally prescribed selection method based on age groups. This prevents targeting specific employees</li>
<li><strong>Herplaatsingsplicht (Redeployment obligation):</strong> Before dismissing anyone, you must genuinely explore whether affected employees can be redeployed to other suitable positions within the organization, including with reasonable retraining</li>
</ul>

<h2>WMCO: Collective Redundancy Notification</h2>
<p>If you plan to dismiss <strong>20 or more employees</strong> within a 3-month period within one UWV region, the WMCO (Wet Melding Collectief Ontslag) applies:</p>
<ul>
<li><strong>Notify UWV and unions:</strong> Before any individual dismissal procedures begin</li>
<li><strong>Mandatory 1-month waiting period:</strong> To allow consultation with unions about alternatives and social plan negotiations</li>
<li><strong>Works council advisory right:</strong> Under Article 25 WOR, the OR must provide formal advice on significant organizational changes. Proceeding without this advice (or ignoring it) gives the OR grounds to challenge the decision in court</li>
</ul>

<h2>Social Plans and Transition Payments</h2>
<p>The financial aspects of Dutch restructuring are substantial:</p>
<ul>
<li><strong>Transitievergoeding (Transition payment):</strong> Legally required for every dismissed employee. Calculated as ⅓ monthly salary per year of service, capped at €94,000 (2024) or one annual salary if higher</li>
<li><strong>Social plan:</strong> For larger restructurings, unions typically negotiate a social plan with enhanced severance, outplacement support, and extended notice periods. These can significantly exceed statutory minimums</li>
<li><strong>Outplacement:</strong> Offering professional career transition support is standard practice and viewed favorably by UWV and courts</li>
</ul>"""
    },
    "anti-discrimination-dutch-workplace": {
        "content": """<h2>Dutch Anti-Discrimination Framework</h2>
<p>The Netherlands has one of Europe's most comprehensive anti-discrimination frameworks, with <strong>multiple overlapping laws</strong> protecting employees from discrimination on a wide range of grounds. For employers, this means proactive compliance — not just reacting to complaints, but actively preventing discrimination in all employment practices.</p>
<p>The primary legislation includes:</p>
<ul>
<li><strong>Algemene wet gelijke behandeling (AWGB):</strong> General Equal Treatment Act — prohibits discrimination on religion, belief, political opinion, race, sex, nationality, sexual orientation, and civil status</li>
<li><strong>Wet gelijke behandeling op grond van leeftijd (WGBL):</strong> Age discrimination protection</li>
<li><strong>Wet gelijke behandeling op grond van handicap of chronische ziekte (WGBH/CZ):</strong> Disability and chronic illness discrimination protection</li>
<li><strong>Article 7:646 BW:</strong> Equal treatment of men and women in employment</li>
</ul>

<h2>Where Discrimination Risks Arise</h2>
<p>Discrimination claims can emerge at every stage of the employment lifecycle:</p>
<ul>
<li><strong>Recruitment:</strong> Job advertisements cannot contain discriminatory requirements (age limits, nationality preferences, gender specifications). "Young and dynamic team" is widely considered age discrimination</li>
<li><strong>Selection procedures:</strong> Unconscious bias in CV screening and interviews is a major risk area. The Dutch College voor de Rechten van de Mens (Human Rights Board) regularly rules on recruitment discrimination cases</li>
<li><strong>Pay equity:</strong> The Netherlands is implementing EU Pay Transparency Directive requirements. Unjustified pay differences between employees in comparable roles constitute discrimination</li>
<li><strong>Promotion and development:</strong> Systematic exclusion of certain groups from career opportunities creates indirect discrimination claims</li>
<li><strong>Termination:</strong> Dismissal that disproportionately affects protected groups may be challenged as discriminatory redundancy</li>
</ul>

<h2>Employer Obligations: Proactive Prevention</h2>
<p>Dutch law requires more than passive non-discrimination — employers must actively work to prevent discrimination:</p>
<ul>
<li><strong>Vertrouwenspersoon (Confidential advisor):</strong> As of January 2024, employers must offer access to a confidential advisor for employees experiencing discrimination or harassment. This is now mandatory under the amended Arbeidsomstandighedenwet</li>
<li><strong>Complaint procedure:</strong> Establish a clear, documented procedure for reporting and investigating discrimination complaints</li>
<li><strong>Training:</strong> Regular bias awareness and anti-discrimination training for managers involved in hiring and personnel decisions</li>
<li><strong>Policy documentation:</strong> Include anti-discrimination commitments in your employee handbook and ensure all employees acknowledge them</li>
</ul>

<h2>Consequences of Non-Compliance</h2>
<p>Discrimination violations carry significant consequences:</p>
<ul>
<li><strong>Human Rights Board rulings:</strong> While not legally binding, these carry strong moral authority and are frequently cited in court proceedings</li>
<li><strong>Court claims:</strong> Employees can seek compensation for material and immaterial damages. Awards for emotional distress (immateriële schade) in discrimination cases are increasing</li>
<li><strong>Unfair dismissal reversal:</strong> If a termination is found to be discriminatory, courts can reinstate the employee or award enhanced severance (up to 1.5× the transition payment as a "billijke vergoeding")</li>
<li><strong>Reputational risk:</strong> In the Netherlands' transparent business culture, discrimination cases attract significant media and social media attention</li>
</ul>"""
    },
    "expat-employee-management-netherlands": {
        "content": """<h2>Managing International Employees in the Netherlands</h2>
<p>The Netherlands is home to one of Europe's most international workforces — particularly in Amsterdam, The Hague, Rotterdam, and Eindhoven. Managing expat employees effectively requires navigating a complex intersection of <strong>immigration law, tax optimization, cultural integration, and Dutch employment regulations</strong>.</p>
<p>For international companies establishing Dutch operations, the expat workforce is often your founding team. Getting their setup right from day one prevents costly corrections later and sets the tone for your entire Netherlands operation.</p>

<h2>Immigration and Work Permits</h2>
<p>The type of work authorization depends on the employee's nationality and situation:</p>
<ul>
<li><strong>EU/EEA nationals:</strong> Free to work without permits. Registration with the municipality (Gemeente) for a BSN number is sufficient</li>
<li><strong>Highly Skilled Migrant (KM):</strong> The most common route for non-EU knowledge workers. Requires IND-recognized sponsor status for the employer and minimum salary thresholds (€5,331/month for 30+ years old, €3,909 for under 30, 2024 rates)</li>
<li><strong>Intra-Company Transfer (ICT):</strong> For executives, managers, and specialists transferring within a multinational. Maximum 3 years for managers/specialists, 1 year for trainees</li>
<li><strong>Orientation Year (Zoekjaar):</strong> Recent graduates of Dutch universities can obtain a 1-year residence permit to find qualifying employment</li>
</ul>

<h2>The 30% Ruling: Maximizing Tax Efficiency</h2>
<p>The 30% ruling (30%-regeling) is the Netherlands' flagship tax incentive for incoming foreign employees:</p>
<ul>
<li><strong>Benefit:</strong> 30% of gross salary is paid tax-free as a deemed reimbursement for "extraterritorial costs." Effectively reduces the tax burden by approximately 10-15% depending on income level</li>
<li><strong>Duration:</strong> Maximum 5 years (reduced from the previous 8 years)</li>
<li><strong>Eligibility:</strong> Employee must have specific expertise not readily available in the Dutch labor market, have lived 150+ km from the Dutch border for 16 of the 24 months prior to employment, and meet the minimum salary requirement</li>
<li><strong>2024 changes:</strong> The ruling is now capped — only the first 30% is fully exempt, then reduced to 20% and 10% in subsequent periods. Check current legislation for exact thresholds</li>
</ul>

<h2>Relocation Support and Cultural Integration</h2>
<p>Successful expat management goes beyond legal compliance:</p>
<ul>
<li><strong>Housing support:</strong> The Dutch housing market is extremely tight in major cities. Provide broker assistance, temporary housing, and realistic budget guidance</li>
<li><strong>Partner support:</strong> Expat partner satisfaction is the #1 predictor of assignment success. Offer career coaching, language courses, and social integration support for accompanying partners</li>
<li><strong>Dutch language and culture:</strong> While business is commonly conducted in English, expats who learn Dutch integrate better and stay longer. Sponsor language courses as a standard benefit</li>
<li><strong>BSN and DigiD:</strong> Every resident needs a Burger Service Nummer (BSN) for tax, banking, and healthcare. The DigiD provides digital access to government services. Help employees navigate these processes promptly</li>
<li><strong>Healthcare setup:</strong> Dutch mandatory health insurance (basisverzekering) must be arranged within 4 months of registration. Guide employees through the selection process</li>
</ul>"""
    },
    # ===== HR S.O.S. — 14 thin pages =====
    "emergency-dismissal-netherlands": {
        "content": """<h2>When Can You Dismiss on the Spot?</h2>
<p>Ontslag op staande voet (summary dismissal) is the most extreme measure in Dutch employment law — and the most legally risky. It must only be used for <strong>dringende redenen (urgent reasons)</strong> so serious that you cannot reasonably be expected to continue the employment relationship for even one more day.</p>
<p>Dutch courts interpret "urgent reasons" very strictly. What might justify immediate termination in other countries often fails to meet the Dutch legal threshold. Getting it wrong means the dismissal is void, and you face claims for back pay, transition payment, and a "billijke vergoeding" (fair compensation) penalty.</p>

<h2>Legal Requirements for Valid Summary Dismissal</h2>
<p>All three conditions must be met simultaneously — failing any one invalidates the entire dismissal:</p>
<ul>
<li><strong>Urgent reason (Dringende reden):</strong> The conduct must be so serious that immediate termination is the only proportionate response. Examples include theft, fraud, physical violence, gross insubordination, or working under the influence. Performance issues, personality conflicts, and single incidents of misconduct almost never qualify</li>
<li><strong>Immediacy (Onverwijldheid):</strong> You must act immediately after discovering the urgent reason. Even a delay of 2-3 days can invalidate the dismissal. If you need time to investigate, suspend the employee with pay while you gather evidence — but communicate the dismissal decision the moment your investigation confirms the facts</li>
<li><strong>Immediate communication (Onverwijlde mededeling):</strong> The employee must be told immediately why they're being dismissed. The stated reason becomes the basis for any legal challenge — you cannot add new reasons later. Prepare your statement carefully before the conversation</li>
</ul>

<h2>Examples from Dutch Case Law</h2>
<p>Courts have established extensive precedent on what does and doesn't justify summary dismissal:</p>
<ul>
<li><strong>Accepted:</strong> Embezzlement/theft (even small amounts), deliberate fraud, violent threats or assault against colleagues, persistent refusal to follow reasonable instructions after formal warnings, serious safety violations</li>
<li><strong>Rejected:</strong> Single instances of tardiness, using company internet for personal purposes, one-time emotional outburst, alleged underperformance without improvement trajectory, social media posts critical of the company</li>
<li><strong>Context-dependent:</strong> Courts consider the employee's length of service, prior record, personal circumstances, and the proportionality of dismissal versus a lesser sanction. A 20-year veteran with a clean record faces a higher threshold than a new hire</li>
</ul>

<h2>The Investigation and Documentation Process</h2>
<p>Before pulling the trigger on summary dismissal, you need bulletproof documentation:</p>
<ul>
<li><strong>Gather evidence first:</strong> Security footage, digital logs, witness statements. Hearsay and assumptions will not survive legal challenge</li>
<li><strong>Suspend pending investigation:</strong> Send the employee home with full pay while you investigate. This preserves your right to act "immediately" once facts are confirmed</li>
<li><strong>Legal review:</strong> Have an employment lawyer review your case before proceeding. The cost of legal advice is minimal compared to the cost of a wrongful dismissal claim</li>
<li><strong>Witness the conversation:</strong> Always have HR or another manager present during the dismissal conversation. Document the meeting in a written confirmation letter, delivered the same day</li>
</ul>"""
    },
    "settlement-agreement-netherlands": {
        "content": """<h2>What Is a Vaststellingsovereenkomst?</h2>
<p>A vaststellingsovereenkomst (settlement agreement, or VSO) is the most common way to end employment in the Netherlands by mutual agreement. It's used in approximately <strong>70% of all employment terminations</strong> — more than court proceedings and UWV permits combined. The VSO allows both parties to negotiate terms and avoid the uncertainty and cost of legal proceedings.</p>
<p>For employers, the VSO offers control and predictability. For employees, it typically provides a better financial package than a court-ordered dismissal. When done correctly, it's a clean exit for everyone.</p>

<h2>Essential Terms Every VSO Must Contain</h2>
<p>A well-drafted settlement agreement addresses all aspects of the employment termination:</p>
<ul>
<li><strong>Termination date:</strong> Must respect the statutory notice period (typically 1-3 months depending on tenure). If the notice period isn't honored, the employee may lose their right to unemployment benefits (WW-uitkering)</li>
<li><strong>Reason for termination:</strong> Always state that the initiative came from the employer for business-economic or work-related reasons. Never attribute blame to the employee — this protects their UWV benefits eligibility</li>
<li><strong>Severance payment:</strong> At minimum, the statutory transition payment (transitievergoeding). In practice, negotiated amounts range from 1× to 2× the statutory amount, depending on circumstances</li>
<li><strong>Final salary settlement:</strong> Outstanding salary, accrued vacation days, pro-rated vakantiegeld (holiday allowance), and any bonus entitlements</li>
<li><strong>Garden leave (Vrijstelling van werk):</strong> Whether the employee works during the notice period or is released with pay. Most VSOs release the employee immediately</li>
<li><strong>Non-compete and non-solicitation:</strong> Whether existing restrictive covenants are maintained, modified, or waived entirely</li>
<li><strong>Reference letter:</strong> Agree on the content and timing of the employment reference</li>
<li><strong>Mutual final discharge (Finale kwijting):</strong> Both parties release each other from all further claims arising from the employment relationship</li>
</ul>

<h2>The 14-Day Cooling-Off Period</h2>
<p>Dutch law provides a critical employee protection: the <strong>bedenktermijn (cooling-off period)</strong>. After signing the VSO, the employee has 14 calendar days to revoke the agreement without giving any reason. This cannot be waived or shortened.</p>
<ul>
<li>The agreement must explicitly mention this right. If it doesn't, the cooling-off period extends to 21 days</li>
<li>An employee can only use this right once in every 6-month period — to prevent abuse</li>
<li>If the employee revokes, the employment relationship continues as if nothing happened</li>
</ul>
<p>For employers, this means you shouldn't announce the departure externally or begin replacement hiring until the cooling-off period expires.</p>

<h2>Protecting Employee WW Benefits</h2>
<p>A properly drafted VSO preserves the employee's right to WW (unemployment) benefits. Critical requirements:</p>
<ul>
<li><strong>Employer initiative:</strong> The termination must be framed as the employer's decision, not a mutual desire or employee request</li>
<li><strong>No urgent reason:</strong> The VSO cannot cite misconduct (dringende reden) — this disqualifies WW benefits</li>
<li><strong>Notice period compliance:</strong> The fictive notice period must be respected. If the statutory period is 2 months but the VSO terminates effective immediately, the employee cannot claim WW for those 2 months</li>
<li><strong>Seek legal advice:</strong> Employees should always have the VSO reviewed by a lawyer. Many employers cover legal costs (typically €750-1,500 ex VAT) as part of the package</li>
</ul>"""
    },
    "dutch-employment-law-urgent-questions": {
        "content": """<h2>Most Common Urgent Employment Law Situations</h2>
<p>Employment crises rarely arrive with advance warning. Whether it's an employee who disappears without notice, a sudden allegation of misconduct, or a confused manager making promises they shouldn't — <strong>the first 24-48 hours of an employment law crisis determine the outcome</strong>.</p>
<p>Dutch employment law is heavily procedural. The steps you take (or fail to take) immediately after an incident can either protect your rights or permanently waive them. This guide covers the situations we see most frequently and what to do right now.</p>

<h2>Employee Refuses to Work</h2>
<p>An employee stops performing their duties or refuses reasonable instructions. Your response must be measured and documented:</p>
<ul>
<li><strong>Immediate step:</strong> Confirm the instruction in writing and ask the employee to explain their refusal in writing</li>
<li><strong>Formal warning:</strong> Issue a written warning specifying the refusal and its consequences. State clearly that continued refusal may result in wage suspension or disciplinary action</li>
<li><strong>Wage suspension:</strong> Under Art. 7:627 BW, "no work, no pay" — but only if the refusal is unjustified and you've given proper notice</li>
<li><strong>Do NOT dismiss on the spot</strong> unless the refusal constitutes an "urgent reason" (which is rare for work refusal alone). Instead, build a dossier and pursue a kantonrechter procedure</li>
</ul>

<h2>Employee Goes AWOL</h2>
<p>When an employee simply stops showing up:</p>
<ul>
<li><strong>Day 1:</strong> Attempt contact via phone, email, and emergency contact. Document every attempt</li>
<li><strong>Day 2-3:</strong> Send a registered letter (aangetekende brief) to their home address. Request they report to work and explain that unauthorized absence may have consequences</li>
<li><strong>Week 1:</strong> If no response, send a second registered letter warning that continued absence without valid reason may lead to wage suspension and dismissal proceedings</li>
<li><strong>After 2+ weeks:</strong> Consider whether the absence constitutes abandonment of employment. Even then, follow formal dismissal procedures — do not assume the employment has ended</li>
</ul>

<h2>Allegations of Harassment or Discrimination</h2>
<p>Receiving a formal or informal complaint about harassment (seksuele intimidatie) or discrimination:</p>
<ul>
<li><strong>Take every complaint seriously:</strong> Even informal mentions. Document that the complaint was received and when</li>
<li><strong>Engage the vertrouwenspersoon:</strong> Support the complainant in accessing the confidential advisor</li>
<li><strong>Investigate promptly:</strong> Conduct a fair investigation — hear both sides, maintain confidentiality, and document findings</li>
<li><strong>Take proportionate action:</strong> Based on findings, implement corrective measures. These can range from mediation to formal warnings to dismissal for serious cases</li>
<li><strong>Protect the complainant:</strong> Ensure no retaliation occurs. Victimization of a complainant is itself a legal violation</li>
</ul>

<h2>Manager Makes Unauthorized Commitments</h2>
<p>A manager promises a raise, promotion, or changed working conditions without HR or director approval:</p>
<ul>
<li><strong>The risk:</strong> Under Dutch law, oral commitments by someone with apparent authority (schijn van volmacht) can be legally binding. If the employee reasonably believed the manager had authority, you may be bound</li>
<li><strong>Immediate response:</strong> Don't immediately contradict the manager. Instead, communicate that the matter needs formal review and approval</li>
<li><strong>Prevention:</strong> Clearly define and communicate managerial authority limits. Include standard contract language stating that HR/director approval is required for any changes to employment terms</li>
</ul>"""
    },
    "handling-workplace-conflict-netherlands": {
        "content": """<h2>Workplace Conflict in Dutch Employment Law</h2>
<p>The Netherlands has a distinctive approach to workplace conflict: <strong>employers are legally required to make genuine efforts to resolve disputes</strong> before considering termination. This obligation stems from the "goed werkgeverschap" principle and the "verstoorde arbeidsverhouding" (disrupted employment relationship) dismissal ground.</p>
<p>A Dutch court will not grant a dismissal based on a disrupted relationship unless the employer can demonstrate that all reasonable measures to repair the relationship have been exhausted. Simply documenting that "the relationship is irreparably damaged" without evidence of resolution attempts guarantees a failed dismissal request.</p>

<h2>Structured Conflict Resolution Approach</h2>
<p>Follow this framework to address workplace conflicts properly:</p>
<ul>
<li><strong>Early intervention:</strong> Address tensions as soon as they emerge. Informal conversations, documented by email, showing you acknowledged and addressed the situation early</li>
<li><strong>Document everything:</strong> Keep written records of incidents, conversations, and actions taken. Courts rely heavily on documentation when assessing whether the employer acted reasonably</li>
<li><strong>Hear both sides:</strong> Under Dutch labor law principles of fairness, every party in a conflict must have the opportunity to share their perspective. One-sided conclusions are viewed negatively by courts</li>
<li><strong>Vertrouwenspersoon:</strong> Ensure employees know they can consult the confidential advisor (now mandatory). This provides a safe channel for concerns before they escalate</li>
</ul>

<h2>Mediation: The Expected Standard</h2>
<p>Dutch courts view mediation as an <strong>essential step</strong> before any termination based on a disrupted working relationship:</p>
<ul>
<li><strong>Certified mediation:</strong> Use an MfN-registered mediator (Mediators federatie Nederland). Courts give significantly more weight to professional mediation than informal talks</li>
<li><strong>Genuine participation:</strong> Both parties must participate in good faith. An employer who goes through mediation "for show" — having already decided to dismiss — will be exposed and penalized</li>
<li><strong>Confidentiality:</strong> Mediation discussions are confidential and cannot be used in court proceedings. This is crucial for creating a safe space for honest dialogue</li>
<li><strong>Outcome documentation:</strong> If mediation fails, document that it was attempted, who participated, and that no resolution was reached (without disclosing content)</li>
</ul>

<h2>When Conflict Becomes Grounds for Dismissal</h2>
<p>If genuine resolution efforts have failed, you may pursue dismissal on the "verstoorde arbeidsverhouding" ground (Article 7:669 lid 3 sub g BW). Courts evaluate:</p>
<ul>
<li>Whether the disruption is <strong>serious and permanent</strong> (not temporary or emotional)</li>
<li>Whether the employer made sufficient efforts to <strong>repair the relationship</strong> (mediation, coaching, role adjustments)</li>
<li>Whether <strong>redeployment</strong> to another position was explored</li>
<li>Whether the employer itself contributed to or caused the conflict</li>
</ul>
<p>If the court finds the employer significantly contributed to the conflict, it may award an enhanced "billijke vergoeding" (fair compensation) on top of the statutory transition payment.</p>"""
    },
    "employee-fraud-investigation-netherlands": {
        "content": """<h2>Responding to Suspected Employee Fraud</h2>
<p>Discovering potential fraud by an employee triggers one of the most high-stakes processes in Dutch employment law. The temptation to act immediately — confronting the employee, locking them out of systems, or terminating on the spot — is understandable but <strong>legally dangerous</strong>. Dutch law requires careful, documented investigation before any disciplinary action.</p>
<p>The key tension: you need to act quickly enough to prevent further damage, but methodically enough to build a case that survives legal scrutiny. Getting this balance wrong can make criminal prosecution impossible, invalidate your dismissal, and expose you to wrongful termination claims.</p>

<h2>The Investigation Framework</h2>
<p>Follow these steps to conduct a legally defensible fraud investigation:</p>
<ul>
<li><strong>Secure evidence immediately:</strong> Preserve digital evidence (emails, system logs, financial records) before the suspect realizes they're under investigation. Your IT team should create forensic copies — not original files that could be challenged as tampered</li>
<li><strong>Suspend, don't dismiss:</strong> Suspend the employee with full pay pending investigation. This is legally safe and gives you time to investigate properly. A hasty dismissal that fails in court is far more costly than a few weeks of paid suspension</li>
<li><strong>Privacy compliance (AVG/GDPR):</strong> Your investigation must comply with Dutch privacy law. You can review company systems and communications (if your policy permits), but personal devices and communications have stronger protections. Document your legal basis for each investigative step</li>
<li><strong>Consider external investigators:</strong> For significant fraud, engage a forensic accounting firm or corporate investigation agency. Their findings carry more weight in court than internal conclusions</li>
</ul>

<h2>Legal Considerations During Investigation</h2>
<p>Dutch employment law and criminal law intersect in fraud cases:</p>
<ul>
<li><strong>Criminal reporting:</strong> You have no legal obligation to report fraud to police, but failure to do so may complicate insurance claims and could be raised in employment proceedings</li>
<li><strong>Self-incrimination:</strong> Unlike criminal proceedings, there's no right against self-incrimination in internal investigations. However, evidence obtained under duress (threats, intimidation) will be excluded</li>
<li><strong>Proportionality:</strong> Your investigative measures must be proportionate to the suspected fraud. covert surveillance or monitoring requires a very strong justification and proper privacy impact assessment</li>
<li><strong>Employee rights:</strong> The suspected employee has the right to know the allegations against them and respond. This doesn't mean you reveal everything immediately — but before any final decision, they must have the opportunity to explain</li>
</ul>

<h2>Taking Action After Investigation</h2>
<p>Once your investigation is complete, your options include:</p>
<ul>
<li><strong>Summary dismissal (ontslag op staande voet):</strong> Appropriate for clear, proven fraud cases. Remember all three requirements: urgent reason, immediacy, and immediate communication</li>
<li><strong>Settlement agreement:</strong> Often preferred for cases where evidence is strong but not airtight. Allows a clean exit without the risk of a failed court challenge</li>
<li><strong>Formal warning and monitoring:</strong> For minor or unintentional transgressions, a formal warning with enhanced oversight may be proportionate</li>
<li><strong>Recovery of damages:</strong> The employer can pursue civil recovery of stolen or embezzled funds, either through court or as part of a settlement</li>
</ul>"""
    },
    "sick-employee-not-cooperating": {
        "content": """<h2>Understanding the Reintegration Framework</h2>
<p>Dutch sick leave law places extensive obligations on <strong>both employer and employee</strong>. Under the Wet verbetering poortwachter (Gatekeeper Improvement Act), a sick employee must actively cooperate with their reintegration into work. When an employee refuses to cooperate, you have legal tools to address this — but the process requires careful, documented steps.</p>
<p>Non-cooperation can take many forms: refusing to visit the company doctor (bedrijfsarts), declining suitable alternative work, not responding to communications, ignoring the reintegration plan, or providing inconsistent information about their condition.</p>

<h2>Step-by-Step Response to Non-Cooperation</h2>
<p>Before using sanctions, you must follow a structured escalation process:</p>
<ul>
<li><strong>Step 1 — Informal conversation:</strong> Discuss the issue directly. Often, non-cooperation stems from fear, miscommunication, or genuine disagreement about fitness for work. Document the conversation in writing</li>
<li><strong>Step 2 — Company doctor assessment:</strong> Request a bedrijfsarts evaluation of the employee's abilities and limitations. The doctor provides a medisch advies (medical advice) on what the employee can reasonably be expected to do</li>
<li><strong>Step 3 — Written warning:</strong> If the employee disregards the company doctor's advice, send a formal written warning. Clearly state which reintegration obligation they're violating and what will happen if non-cooperation continues</li>
<li><strong>Step 4 — Wage suspension:</strong> Under Article 7:629 lid 3 BW, you may suspend salary payments if the employee refuses to cooperate with reintegration. You must give written advance notice before implementing this, specifying the reason</li>
<li><strong>Step 5 — Wage cessation vs. suspension:</strong> There's an important legal distinction: suspension (opschorting) means you withhold pay that becomes due when the employee cooperates. Cessation (stopzetting) means the employee permanently loses the right to pay for the non-cooperation period</li>
</ul>

<h2>The Deskundigenoordeel (Expert Opinion)</h2>
<p>When there's disagreement about the employee's ability to work, either party can request a <strong>deskundigenoordeel from UWV</strong>. This is an independent second opinion that carries significant weight:</p>
<ul>
<li>The employee may request one if they disagree with the company doctor's assessment</li>
<li>The employer may request one to strengthen their position before implementing wage sanctions</li>
<li>Courts view the deskundigenoordeel as critical evidence — acting without one (when available) weakens your position significantly</li>
</ul>

<h2>Dismissal for Persistent Non-Cooperation</h2>
<p>If sanctions fail and the employee continues to refuse cooperation, dismissal becomes an option:</p>
<ul>
<li><strong>Via kantonrechter:</strong> Request contract dissolution based on the employee's failure to cooperate with reasonable reintegration requirements</li>
<li><strong>Evidence required:</strong> Documentation of the entire escalation process, company doctor reports, warnings, wage measures taken, and deskundigenoordeel (if obtained)</li>
<li><strong>Transition payment:</strong> Courts may deny or reduce the transition payment if the employee's non-cooperation constitutes "seriously culpable conduct" (ernstig verwijtbaar handelen)</li>
</ul>"""
    },
    "reorganization-crisis-netherlands": {
        "content": """<h2>When Crisis Hits: Navigating Dutch Reorganization</h2>
<p>A crisis-driven reorganization — whether triggered by sudden revenue decline, loss of a major client, regulatory changes, or market disruption — requires rapid action within extremely structured legal boundaries. Dutch law does not have "at-will" dismissal, meaning even in emergencies, you <strong>must follow the full procedural framework</strong>.</p>
<p>The speed at which you can restructure depends on preparation. Companies with proactive HR legal support can execute a reorganization in 6-8 weeks. Those starting from zero may need 3-6 months — time that can be devastating during a crisis.</p>

<h2>Immediate Actions (Week 1-2)</h2>
<p>When the decision to reorganize is unavoidable:</p>
<ul>
<li><strong>Engage legal counsel immediately:</strong> Before any internal communication, ensure your employment lawyer is briefed. Premature announcements can trigger legal obligations and create panic</li>
<li><strong>Assess the scale:</strong> Determine whether the WMCO (Wet Melding Collectief Ontslag) applies — dismissal of 20+ employees in 3 months within one UWV region. This fundamentally changes the process and timeline</li>
<li><strong>Works council notification:</strong> Under Article 25 WOR, the OR must be consulted on significant organizational changes. The advisory process takes minimum 4-6 weeks for complex restructurings</li>
<li><strong>Financial documentation:</strong> Compile profit/loss statements, cash flow projections, market analysis, and a clear business case. UWV will scrutinize these documents</li>
</ul>

<h2>The WMCO Collective Dismissal Process</h2>
<p>If the WMCO threshold is triggered, additional obligations apply:</p>
<ul>
<li><strong>Notification to UWV and unions:</strong> Formal written notification before individual procedures begin. Must include the reason, number of affected employees, selection criteria, and proposed timeline</li>
<li><strong>One-month waiting period:</strong> From notification to unions, you must wait at least one month before submitting individual UWV dismissal applications</li>
<li><strong>Union consultation:</strong> Unions (typically FNV, CNV) will want to negotiate a social plan. Even if your company has no CLA, unions representing your employees have consultation rights</li>
<li><strong>Employee selection:</strong> The afspiegelingsbeginsel (reflection principle) determines who is selected for dismissal. Employees are grouped by interchangeable function, then within each group, selection is based on age cohorts using a last-in-first-out principle within each cohort</li>
</ul>

<h2>Social Plan Negotiations</h2>
<p>For significant restructurings, a social plan (sociaal plan) sets enhanced terms for departing employees:</p>
<ul>
<li><strong>Enhanced severance:</strong> Typically 1-2 months' salary per year of service, beyond the statutory transition payment</li>
<li><strong>Outplacement support:</strong> Professional career transition coaching, typically 3-6 months</li>
<li><strong>Extended notice period:</strong> Additional time for job searching</li>
<li><strong>Retraining budgets:</strong> Education allowances for employees transitioning to new careers</li>
<li><strong>Hardship clause:</strong> Individual exception provisions for employees in particularly difficult circumstances</li>
</ul>"""
    },
    "discrimination-complaint-handling": {
        "content": """<h2>Handling Discrimination Complaints Properly</h2>
<p>Receiving a discrimination complaint is a critical moment for any organization. How you handle it determines not only the legal outcome but also your company culture, employee trust, and reputation. Under Dutch law, employers have a <strong>duty of care (zorgplicht)</strong> to provide a safe, discrimination-free workplace — and that includes having a robust, fair complaint process.</p>
<p>Since January 2024, every employer is legally required to provide access to a vertrouwenspersoon (confidential advisor) for employees experiencing harassment or discrimination. This is your first line of defense and support.</p>

<h2>The Complaint Process: Step by Step</h2>
<p>A proper internal complaint procedure for discrimination includes:</p>
<ul>
<li><strong>Intake and acknowledgment:</strong> Acknowledge the complaint within 48 hours. The complainant should know their report has been received and will be taken seriously</li>
<li><strong>Confidential advisor engagement:</strong> The vertrouwenspersoon provides emotional support, explains procedures, and helps the complainant decide whether to file a formal complaint</li>
<li><strong>Investigation committee:</strong> For formal complaints, appoint an impartial investigation committee (klachtencommissie). Consider using external investigators for objectivity, especially for complaints against senior management</li>
<li><strong>Hear both parties:</strong> Both the complainant and the accused must have the opportunity to present their version. This is a fundamental principle of Dutch administrative fairness (hoor en wederhoor)</li>
<li><strong>Investigation report:</strong> Document findings, including evidence reviewed, witness statements, and conclusions. The report should state whether discrimination occurred and recommend actions</li>
<li><strong>Decision and action:</strong> Management decides on corrective measures based on the investigation findings. Actions range from mediation and training to formal warnings and dismissal</li>
</ul>

<h2>External Remedies Available to Employees</h2>
<p>Employees who feel their complaint was not properly handled have external escalation paths:</p>
<ul>
<li><strong>College voor de Rechten van de Mens:</strong> The Netherlands Institute for Human Rights investigates discrimination complaints. Their opinions, while not legally binding, are authoritative and frequently cited by courts</li>
<li><strong>Kantonrechter (Subdistrict Court):</strong> Employees can pursue financial compensation for damages through court proceedings</li>
<li><strong>Arbeidsinspectie:</strong> The Dutch Labour Inspectorate can investigate whether the employer met their duty of care obligations regarding workplace safety and discrimination prevention</li>
<li><strong>Police and public prosecutor:</strong> In severe cases (hate crimes, sexual assault), criminal prosecution is possible alongside workplace procedures</li>
</ul>

<h2>Building a Prevention-First Culture</h2>
<p>The best complaint handling is prevention:</p>
<ul>
<li><strong>Regular training:</strong> Anti-discrimination and unconscious bias training for all employees, with additional focus for hiring managers</li>
<li><strong>Diversity policy:</strong> Publish and implement a diversity and inclusion policy. This demonstrates institutional commitment</li>
<li><strong>Anonymous reporting:</strong> Provide secure, anonymous channels for reporting concerns below the formal complaint threshold</li>
<li><strong>Exit interview analysis:</strong> Systematically analyze exit interview data for patterns that may indicate discrimination or exclusion</li>
<li><strong>Celebrate diversity:</strong> Active cultural events and Employee Resource Groups (ERGs) signal genuine commitment beyond policy documents</li>
</ul>"""
    },
    "works-council-dispute-resolution": {
        "content": """<h2>When Management and Works Council Disagree</h2>
<p>The relationship between management and the ondernemingsraad (OR/works council) is a cornerstone of Dutch corporate governance. But disagreements are inevitable — and Dutch law provides a sophisticated framework for resolving disputes that protects both the OR's participation rights and the company's ability to operate effectively.</p>
<p>Understanding this framework is essential because <strong>ignoring OR rights can invalidate business decisions</strong>, no matter how commercially sensible they are. Several high-profile Dutch cases have seen court orders reversing mergers, restructurings, and policy changes because the works council's rights were not properly respected.</p>

<h2>OR Rights and When Disputes Arise</h2>
<p>Disputes typically arise in three categories of OR rights:</p>
<ul>
<li><strong>Advisory right (Adviesrecht — Art. 25 WOR):</strong> For significant decisions including restructuring, mergers/acquisitions, major investments, relocations, and changes in organizational structure. The OR advises; management decides</li>
<li><strong>Consent right (Instemmingsrecht — Art. 27 WOR):</strong> For policies on working hours, holiday schemes, health & safety, privacy monitoring, performance evaluation, and complaint procedures. Management cannot implement these without OR consent</li>
<li><strong>Information right (Art. 31 WOR):</strong> The OR has the right to receive financial information, strategic plans, and social policy data. Withholding information undermines the advisory and consent processes</li>
</ul>

<h2>Dispute Resolution Mechanisms</h2>
<p>When agreement cannot be reached, Dutch law provides several escalation paths:</p>
<ul>
<li><strong>Mediative discussions:</strong> Many disputes are resolved through extended dialogue. The SER (Sociaal-Economische Raad) provides mediation support specifically for OR disputes</li>
<li><strong>Bedrijfscommissie:</strong> Sector-specific dispute committees that mediate between OR and management. Often effective for procedural disputes</li>
<li><strong>Kantonrechter (Advisory right disputes):</strong> Under Art. 26 WOR, if the OR believes its advisory right was inadequately followed, it can challenge the decision in court. The court can order the employer to reverse the decision or halt implementation</li>
<li><strong>Kantonrechter (Consent right disputes):</strong> Under Art. 27 lid 5 WOR, if the OR withholds consent, the employer can request the court to substitute consent, but only if the OR's refusal is unreasonable or the employer has compelling grounds</li>
<li><strong>Ondernemingskamer (Enterprise Chamber):</strong> The Amsterdam Court of Appeal's specialized business chamber handles complex corporate governance disputes, including OR involvement in fundamental corporate changes</li>
</ul>

<h2>Best Practices for Preventing Disputes</h2>
<p>Prevention is always preferable to litigation:</p>
<ul>
<li><strong>Involve the OR early:</strong> Don't present decisions as fait accompli. Engage during the planning phase so advice genuinely influences outcomes</li>
<li><strong>Provide complete information:</strong> Partial or delayed information creates suspicion. Share what you can, when you can, and explain any confidentiality restrictions</li>
<li><strong>Respect timelines:</strong> OR processes take time. Build advisory and consent timelines into your project planning</li>
<li><strong>Training for both sides:</strong> Invest in OR training (which is the employer's legal obligation) and train management on working effectively with the OR</li>
</ul>"""
    },
    "non-compete-enforcement-netherlands": {
        "content": """<h2>Non-Compete Clauses Under Dutch Law</h2>
<p>The concurrentiebeding (non-compete clause) is one of the most frequently litigated employment provisions in Dutch law. While enforceable in principle, Dutch courts increasingly scrutinize these clauses and frequently limit or void them — particularly when they disproportionately restrict an employee's ability to earn a living.</p>
<p>Understanding the current legal landscape is essential: recent developments strongly favor employee mobility, and <strong>proposed legislation may fundamentally change non-compete enforceability</strong> in the coming years.</p>

<h2>Legal Requirements for Valid Non-Compete Clauses</h2>
<p>A non-compete clause must meet several strict requirements to be enforceable:</p>
<ul>
<li><strong>In writing:</strong> Must be included in the signed employment contract. Verbal agreements or handbook references are insufficient</li>
<li><strong>Adult employee:</strong> Only valid for employees aged 18 or older</li>
<li><strong>Fixed-term contracts:</strong> Non-compete clauses in bepaalde tijd (fixed-term) contracts are only valid if the employer provides a written justification of the specific, substantial business interests requiring the restriction. Generic justifications ("to protect our market position") are insufficient</li>
<li><strong>Reasonable scope:</strong> Courts assess duration, geographic scope, and competitive scope. Clauses exceeding 1 year, covering unreasonably large geographic areas, or broadly defining "competition" face a high risk of judicial modification</li>
</ul>

<h2>When Courts Limit or Void Non-Compete Clauses</h2>
<p>Dutch courts regularly exercise their power under Art. 7:653 BW to limit or void non-compete restrictions. Common scenarios:</p>
<ul>
<li><strong>Disproportionate restriction:</strong> If the clause prevents the employee from working in their profession entirely, courts typically narrow it to specific competitors or reduce the duration</li>
<li><strong>Changed function:</strong> If the employee's role changed significantly during employment (promotion, role expansion), the original non-compete may no longer cover the current position. A new clause should be signed for the new role</li>
<li><strong>Short employment:</strong> Courts are more likely to limit clauses for employees with short tenure, as they had less access to trade secrets</li>
<li><strong>Employer's culpable conduct:</strong> If the employer's behavior (poor treatment, broken promises) caused the employee to leave, enforcement of the non-compete may be considered unfair</li>
</ul>

<h2>Enforcement Strategies</h2>
<p>If a former employee violates a valid non-compete clause, your options include:</p>
<ul>
<li><strong>Kort geding (summary proceedings):</strong> Request an injunction from the voorzieningenrechter (preliminary relief judge) to immediately halt the competitive activity. This is the fastest route — typically heard within 2-4 weeks</li>
<li><strong>Contractual penalty (boetebeding):</strong> Claim the agreed penalty for each day/week of violation. The penalty must be separately agreed in the contract and courts can mitigate excessive penalties</li>
<li><strong>Damages claim:</strong> Pursue compensation for actual damages caused by the competitive activity through regular proceedings</li>
<li><strong>Cease-and-desist letter:</strong> Often, a well-crafted legal letter from an employment lawyer is sufficient to stop the violation without court proceedings</li>
</ul>"""
    },
    "whistleblower-protection-netherlands": {
        "content": """<h2>The Dutch Whistleblower Protection Framework</h2>
<p>The Netherlands transposed the EU Whistleblower Directive into Dutch law through the <strong>Wet bescherming klokkenluiders</strong> (Whistleblower Protection Act), which took effect in February 2023. This law significantly expanded protections for employees who report wrongdoing and imposed new obligations on employers.</p>
<p>For companies with <strong>50 or more employees</strong>, compliance is mandatory and involves establishing internal reporting channels, protecting reporters from retaliation, and maintaining confidential investigation procedures. Companies with 250+ employees face stricter requirements for anonymous reporting channels.</p>

<h2>Employer Obligations</h2>
<p>Under the Wet bescherming klokkenluiders, employers must:</p>
<ul>
<li><strong>Establish internal reporting channels:</strong> Create a secure, accessible procedure for employees to report suspected wrongdoing. The channel must allow written and oral reports, and where reasonably possible, in-person meetings</li>
<li><strong>Designate investigators:</strong> Appoint impartial persons to receive and investigate reports. They must have no conflict of interest with the reported matter</li>
<li><strong>Acknowledge receipt:</strong> Confirm receipt of a report within 7 days</li>
<li><strong>Provide feedback:</strong> Inform the reporter about the investigation's progress and outcome within 3 months (extendable to 6 months for complex cases)</li>
<li><strong>Maintain confidentiality:</strong> The reporter's identity must be kept confidential unless they consent to disclosure. Sharing the identity without consent is a violation of the law</li>
<li><strong>Works council involvement:</strong> The reporting procedure requires works council consent under Article 27 WOR. The OR has a genuine say in how the procedure is designed</li>
</ul>

<h2>What Constitutes Protected Reporting</h2>
<p>The law protects reports of suspected wrongdoing that is in the <strong>public interest</strong>. This includes:</p>
<ul>
<li>Criminal offenses or violations of law</li>
<li>Threats to public health, safety, or the environment</li>
<li>Mismanagement or improper use of public funds</li>
<li>Violations of EU law</li>
<li>Actions that deliberately suppress, conceal, or destroy information about the above</li>
</ul>
<p>Important: personal workplace grievances (salary disputes, poor management, interpersonal conflicts) are generally NOT protected under whistleblower legislation unless they also involve broader wrongdoing.</p>

<h2>Anti-Retaliation and Enforcement</h2>
<p>The strongest protection in the law is the <strong>prohibition of retaliation (benadeling)</strong>:</p>
<ul>
<li><strong>Broad definition:</strong> Retaliation includes dismissal, demotion, harassment, disciplinary action, negative performance reviews, transfer, refusal of training, or any other disadvantageous treatment related to the report</li>
<li><strong>Reversed burden of proof:</strong> If a reporter alleges retaliation, the employer must prove that any adverse action was NOT related to the whistleblowing report. This is a significant legal advantage for reporters</li>
<li><strong>Third-party protection:</strong> Colleagues who support the whistleblower, facilitators, and legal advisors are also protected from retaliation</li>
<li><strong>Penalties:</strong> Employers who retaliate face civil liability for damages and potential criminal prosecution</li>
</ul>"""
    },
    "wage-claim-defense-netherlands": {
        "content": """<h2>Understanding Wage Claims in Dutch Employment Law</h2>
<p>A wage claim (loonvordering) arises when an employee alleges they were not paid correctly — whether it's underpayment of base salary, missed overtime compensation, unpaid holiday allowance, incorrect pension contributions, or disputed bonus entitlements. In the Netherlands, wage claims carry <strong>significant financial risk</strong> for employers due to the "wettelijke verhoging" (statutory increase) penalty.</p>
<p>Under Article 7:625 BW, if wages are not paid on time, the employee is entitled to a statutory increase of up to <strong>50% of the overdue amount</strong> as a penalty, plus statutory interest. Courts routinely award this increase, making even modest underpayments expensive.</p>

<h2>Common Sources of Wage Claims</h2>
<p>The most frequent wage disputes we encounter stem from:</p>
<ul>
<li><strong>Overtime miscalculation:</strong> Failing to properly compensate overtime hours, especially when the CLA applies specific overtime rates</li>
<li><strong>Vakantiegeld errors:</strong> Incorrect calculation of the 8% holiday allowance base, or forgetting to include certain salary components</li>
<li><strong>CLA compliance:</strong> Not applying mandatory CLA wage scales, automatic annual increments, or sector-specific allowances</li>
<li><strong>Salary during sick leave:</strong> Underpaying the 70% minimum during the first two years of illness, or not applying the CLA top-up to 100%</li>
<li><strong>Bonus and commission disputes:</strong> Ambiguous bonus criteria leading to disagreements about whether targets were met</li>
<li><strong>Transition payment calculation:</strong> Incorrect calculation of the transitievergoeding at termination, using wrong salary components or service dates</li>
</ul>

<h2>Defending Against Wage Claims</h2>
<p>When you receive a wage claim, your response strategy matters enormously:</p>
<ul>
<li><strong>Don't ignore it:</strong> Failure to respond strengthens the employee's position and increases the statutory penalty. Acknowledge the claim promptly and investigate</li>
<li><strong>Audit your payroll:</strong> Conduct a thorough review of the specific calculations challenged. Compare against the employment contract, applicable CLA, and statutory requirements</li>
<li><strong>Check prescription periods:</strong> Wage claims prescribe after 5 years (Art. 3:307 BW). Claims for periods beyond 5 years ago are time-barred</li>
<li><strong>Document your calculations:</strong> If your payroll is correct, prepare a detailed explanation with supporting documentation. Clear communication can resolve many claims without litigation</li>
<li><strong>Consider settlement:</strong> If the claim has merit, early settlement with a negotiated wettelijke verhoging (courts often moderate the 50% to 10-25%) is usually cheaper than full litigation</li>
</ul>

<h2>Prevention: Payroll Compliance Best Practices</h2>
<p>The best defense against wage claims is preventing them:</p>
<ul>
<li><strong>Regular CLA audits:</strong> Check annually whether a mandatory CLA applies to your business and whether you're complying with its wage scales</li>
<li><strong>Clear employment contracts:</strong> Specify all salary components, bonus criteria, and calculation methods unambiguously</li>
<li><strong>Payroll system verification:</strong> After any system change or update, verify calculations manually for a sample of employees</li>
<li><strong>Annual employee confirmation:</strong> Have employees confirm their annual income statement (jaaropgave) to catch discrepancies early</li>
</ul>"""
    },
    "data-breach-employee-data-netherlands": {
        "content": """<h2>Employee Data Breaches: The Dutch Legal Framework</h2>
<p>A data breach involving employee personal data triggers one of the most time-critical compliance challenges in Dutch employment. The Netherlands' implementation of GDPR through the <strong>Uitvoeringswet AVG</strong>, enforced by the Autoriteit Persoonsgegevens (AP — Dutch Data Protection Authority), imposes strict notification obligations with <strong>severe penalties for non-compliance</strong>.</p>
<p>Employee data is among the most sensitive categories you process — BSN numbers, salary information, medical records (sick leave data), performance evaluations, and personal identification documents. A breach of this data affects not only GDPR compliance but also the trust relationship with your workforce.</p>

<h2>Immediate Response: The First 72 Hours</h2>
<p>When you discover (or should reasonably have discovered) a breach involving employee data:</p>
<ul>
<li><strong>Hour 0-4 — Contain the breach:</strong> Stop the data leak. This might mean revoking access, shutting down a compromised system, or notifying your IT security team. Document every action with timestamps</li>
<li><strong>Hour 4-24 — Assess the breach:</strong> Determine what data was affected, how many employees are involved, and the likely risk to their rights and freedoms. Was it BSN numbers? Bank details? Medical data?</li>
<li><strong>Within 72 hours — Notify AP:</strong> If the breach is likely to result in a risk to employees' rights and freedoms, you must notify the Autoriteit Persoonsgegevens within 72 hours of discovery. The notification must include the nature of the breach, categories and approximate number of affected individuals, likely consequences, and measures taken</li>
<li><strong>Notify affected employees:</strong> If the breach is likely to result in a HIGH risk to their rights and freedoms, you must also notify the affected employees directly, "without undue delay"</li>
</ul>

<h2>When Notification Is Required</h2>
<p>Not every data incident requires notification. The key assessment criteria:</p>
<ul>
<li><strong>AP notification required:</strong> Unauthorized access to payroll data, leaked BSN numbers, compromised medical records, ransomware attack on HR systems, misdirected emails containing personal data</li>
<li><strong>Employee notification required:</strong> Identity theft risk (BSN + date of birth exposed), financial data exposure (bank account numbers), medical record disclosure, data published online or sent to wrong recipients</li>
<li><strong>Internal documentation only:</strong> Brief, contained incidents with no external exposure and no sensitive data categories. Even these must be logged in your data breach register</li>
</ul>

<h2>Penalties and Enforcement</h2>
<p>The AP has been increasingly active in enforcement, with significant fines imposed on Dutch employers:</p>
<ul>
<li><strong>Administrative fines:</strong> Up to €20 million or 4% of global annual turnover for serious GDPR violations</li>
<li><strong>Failure to notify:</strong> Separate fines for not reporting a breach within 72 hours</li>
<li><strong>Employee claims:</strong> Individual employees can claim compensation for material and immaterial (emotional) damages resulting from a breach</li>
<li><strong>Collective actions:</strong> Dutch law allows representative organizations to bring collective claims on behalf of affected individuals</li>
</ul>

<h2>Prevention: Protecting Employee Data</h2>
<p>Robust preventive measures reduce both breach risk and regulatory exposure:</p>
<ul>
<li><strong>Access controls:</strong> Limit access to employee data strictly on a need-to-know basis. Regular access reviews to remove unnecessary permissions</li>
<li><strong>Encryption:</strong> Encrypt HR databases, employee files, and email communications containing personal data</li>
<li><strong>Training:</strong> Regular data protection training for all HR staff and managers who handle employee data</li>
<li><strong>Data Protection Impact Assessment:</strong> Conduct DPIAs for high-risk processing activities like employee monitoring, biometric access systems, or medical data processing</li>
</ul>"""
    },
    "union-negotiation-crisis": {
        "content": """<h2>Navigating Union Negotiations in the Netherlands</h2>
<p>Union relations in the Netherlands follow the "poldermodel" — a consensus-driven approach to labor relations that has historically kept industrial action relatively rare compared to other European countries. However, when negotiations break down, the consequences can be significant: <strong>strikes, work slowdowns, and public disputes</strong> that damage both operations and reputation.</p>
<p>Understanding the Dutch union landscape is essential. The major unions — FNV (largest), CNV, and De Unie — represent workers across all sectors. Even in companies without union members, unions can claim negotiating rights if a CLA (collectieve arbeidsovereenkomst) applies to your sector.</p>

<h2>The CLA Negotiation Process</h2>
<p>Collective labor agreement negotiations in the Netherlands follow a structured process:</p>
<ul>
<li><strong>Notice of termination:</strong> Either party can terminate a CLA, typically with 1-3 months' notice before its expiration date. This triggers the negotiation period</li>
<li><strong>Union demands:</strong> Vakbonden (unions) present their eisen (demands), covering wages, working conditions, working hours, pension, and other terms. These typically exceed what's expected as the final outcome</li>
<li><strong>Employer position:</strong> Werkgeversorganisaties (employer associations) or individual employers present counter-proposals. The gap between positions defines the negotiation space</li>
<li><strong>Negotiation rounds:</strong> Multiple formal and informal meetings over weeks or months. Progress is communicated to union members through ledenraadplegingen (member consultations)</li>
<li><strong>Resultaat (Result):</strong> If agreement is reached, it's presented to union members for a vote. Majority approval makes it binding</li>
</ul>

<h2>When Negotiations Break Down</h2>
<p>If no agreement is reached, the escalation path typically follows:</p>
<ul>
<li><strong>Ultimatum:</strong> Unions set a deadline for the employer to meet minimum demands</li>
<li><strong>Actions short of strike:</strong> Work-to-rule (stiptheidsacties), overtime refusal, wearing protest buttons/clothing, or public demonstrations</li>
<li><strong>Mediation:</strong> Either party can request SER mediation or engage a private mediator before escalating further</li>
<li><strong>Strike (Werkstaking):</strong> The ultimate pressure tool. Dutch law recognizes the right to strike as a fundamental social right (based on the European Social Charter). Courts rarely prohibit strikes but may impose conditions</li>
</ul>

<h2>Employer Rights and Strategic Considerations</h2>
<p>During union conflicts, employers have important tools:</p>
<ul>
<li><strong>Wage deduction during strikes:</strong> You are not required to pay employees for hours not worked during a strike</li>
<li><strong>Injunction (kort geding):</strong> You can seek court intervention if a strike is disproportionate, procedurally improper, or causes excessive damage to third parties. Courts balance the right to strike against proportionality</li>
<li><strong>Communication strategy:</strong> Maintain direct communication with all employees — not just union members. Share your perspective on the negotiations transparently</li>
<li><strong>Business continuity planning:</strong> Prepare contingency plans for critical operations during potential work stoppages</li>
<li><strong>Nawerking (After-effect):</strong> When a CLA expires, its terms continue to apply to existing employees until a new CLA is agreed or individual contract changes are negotiated. You cannot unilaterally reduce CLA conditions</li>
</ul>"""
    },
}

def main():
    for fname in ['hr-teams.json', 'hr-sos.json']:
        fpath = os.path.join(BASE, fname)
        with open(fpath) as f:
            pages = json.load(f)
        
        updated = 0
        for page in pages:
            slug = page['slug']
            if slug in ENRICHMENTS:
                enrich = ENRICHMENTS[slug]
                if 'content' in enrich and len(enrich['content']) > len(page.get('content', '')):
                    page['content'] = enrich['content']
                    updated += 1
                    print(f"  ✅ Enriched {slug} ({len(enrich['content'])} chars)")
        
        with open(fpath, 'w') as f:
            json.dump(pages, f, indent=2, ensure_ascii=False)
        
        print(f"\n{fname}: {updated} pages enriched\n")

if __name__ == '__main__':
    main()
