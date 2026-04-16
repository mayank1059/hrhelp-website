#!/usr/bin/env python3
"""Generate guide hero images using Kie.ai API — corrected polling."""
import requests, time, os, json, sys

API_BASE = "https://api.kie.ai"
API_KEY = "95ed5518f580224ee31b179f803d0685"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
OUTPUT_DIR = "/Users/mayanktewari/Vibe/amsterdamkids/hr/hrhelp-website/public/images/guides"

PROMPTS = {
    # HR SETTLERS (16)
    "starting-business-netherlands-us-company": "Professional photorealistic aerial view of Amsterdam business district with modern office towers reflecting in canals, subtle American and Dutch flags visible on a corporate building entrance, golden hour lighting, blue sky, premium corporate photography style, 4K quality",
    "starting-business-netherlands-uk-company": "Professional photorealistic image of a modern glass office building in Amsterdam with Tower Bridge and Big Ben subtly reflected in the glass facade, business professionals walking outside, warm afternoon light, corporate premium photography, 4K",
    "starting-business-netherlands-german-company": "Professional photorealistic image of a modern shared office space with a window view of Amsterdam canal houses, German engineering blueprints on a desk next to Dutch tulips, warm natural lighting, corporate photography style, 4K",
    "hiring-first-employee-netherlands": "Professional photorealistic image of a diverse hiring team in a bright modern Amsterdam office conducting an interview, glass walls, city skyline visible, warm welcoming atmosphere, employment contract papers on the table, corporate photography, 4K",
    "netherlands-bv-vs-branch-office": "Professional photorealistic image of two modern office buildings side by side in Amsterdam, one larger corporate headquarters and one smaller branch office, beautiful Dutch architecture in background, crystal clear day, business district, 4K",
    "employer-registration-netherlands": "Professional photorealistic image of official Dutch government registration documents and a company stamp on a polished wooden desk, modern office setting with Amsterdam canal view through window, warm lighting, 4K",
    "30-percent-ruling-application-2026": "Professional photorealistic image of a happy international professional arriving at Schiphol Airport with luggage, Amsterdam cityscape in the background, welcoming and optimistic atmosphere, blue sky, warm tones, corporate lifestyle photography, 4K",
    "dutch-payroll-setup-guide": "Professional photorealistic image of a modern Dutch payroll dashboard on a large monitor screen showing salary charts and euro calculations, clean minimalist desk, coffee cup, office plants, natural light streaming in, corporate photography, 4K",
    "starting-business-netherlands-japanese-company": "Professional photorealistic image of a modern Amsterdam office interior with subtle Japanese design elements like a bonsai tree on the desk, canal view through panoramic windows, blend of Dutch and Japanese aesthetics, 4K",
    "starting-business-netherlands-french-company": "Professional photorealistic image of a high-speed train arriving at Amsterdam Centraal station, modern glass station architecture, business travelers with briefcases, dynamic and connected atmosphere, 4K",
    "starting-business-netherlands-indian-company": "Professional photorealistic image of a modern tech office in Amsterdam with a diverse team including Indian professionals working on laptops, colorful modern furniture, canal houses visible through large windows, warm collaborative atmosphere, 4K",
    "starting-business-netherlands-australian-company": "Professional photorealistic image of a video conference screen showing Sydney Opera House on one side and Amsterdam skyline on the other, modern conference room, world clock showing both time zones on the wall, bright corporate setting, 4K",
    "starting-business-netherlands-singapore-company": "Professional photorealistic image of Rotterdam modern Erasmus Bridge and skyline resembling Singapore business district, cargo ships in port, international trade atmosphere, golden hour, corporate photography, 4K",
    "starting-business-netherlands-canadian-company": "Professional photorealistic image of a modern co-working space in Amsterdam with Canadian maple leaf artwork on the wall, multicultural professionals collaborating, large windows overlooking a tree-lined canal, autumn colors, 4K",
    "work-permits-visa-sponsorship-netherlands": "Professional photorealistic image of a Dutch IND immigration office interior, clean and modern, international professionals waiting with documents, digital queue system, professional and organized atmosphere, blue and orange accents, 4K",
    "business-bank-account-netherlands": "Professional photorealistic image of a modern Dutch bank interior with sleek design, a business professional signing documents at a private desk, modern banking aesthetic, glass partitions, warm lighting, 4K",
    # HR TEAMS (15)
    "hr-compliance-checklist-netherlands-2026": "Professional photorealistic image of an HR manager reviewing a digital compliance checklist on a tablet in a modern Dutch office, organized binders in background, green checkmarks visible on screen, clean professional atmosphere, 4K",
    "dutch-employment-contracts-guide": "Professional photorealistic image of Dutch employment contract documents with a professional pen on a clean marble desk, reading glasses nearby, modern office with bookshelves of employment law volumes, warm natural lighting, 4K",
    "dutch-sick-leave-management": "Professional photorealistic image of a caring HR professional reviewing a sick leave management file on laptop, modern office with wellness plants, warm supportive atmosphere, medical certificate document visible on desk, 4K",
    "dutch-termination-procedures": "Professional photorealistic image of a formal but respectful business meeting in a Dutch office, two professionals across a conference table reviewing documents together, large windows with soft diffused light, serious but professional tone, 4K",
    "works-council-requirements-netherlands": "Professional photorealistic image of a works council meeting in a modern Dutch boardroom, diverse group of employees seated around an oval table, democratic and collaborative atmosphere, presentation screen in background, 4K",
    "dutch-holiday-allowance-vakantiegeld": "Professional photorealistic image of a happy Dutch professional planning a vacation at their desk in May, calendar showing May, travel brochures, bright cheerful modern office atmosphere, Amsterdam street visible outside, 4K",
    "dutch-pension-system-employers": "Professional photorealistic image of a financial planning meeting between an HR professional and employee, pension fund charts on a screen, modern Dutch office with green plants, warm trustworthy atmosphere, 4K",
    "employee-handbook-netherlands": "Professional photorealistic image of a beautifully designed employee handbook with a company logo on the cover, placed on a clean desk with a welcome kit, modern onboarding room, bright and welcoming, 4K",
    "dutch-parental-leave-policies": "Professional photorealistic image of a professional parent working from home in the Netherlands, baby playing safely in a modern nursery corner of the home office, laptop with video call, work-life balance atmosphere, warm lighting, 4K",
    "dutch-working-time-regulations": "Professional photorealistic image of a modern digital time tracking system on a tablet mounted near an office entrance, clock showing 5pm, employees leaving a Dutch office at end of workday, healthy work-life balance, 4K",
    "performance-management-dutch-law": "Professional photorealistic image of a positive performance review meeting between a manager and employee in a modern Dutch office, performance charts on screen, constructive dialogue atmosphere, natural light, 4K",
    "dutch-remote-work-policy": "Professional photorealistic image of a Dutch professional working from a cozy Amsterdam apartment with canal view, modern home office setup with ergonomic chair and dual monitors, productive atmosphere, 4K",
    "restructuring-redundancy-netherlands": "Professional photorealistic image of a corporate boardroom with organizational charts and restructuring plans projected on screen, modern Dutch office, serious but forward-looking atmosphere, strategic planning, 4K",
    "anti-discrimination-dutch-workplace": "Professional photorealistic image of a diverse and inclusive Dutch workplace team celebrating together, multicultural group in a modern Amsterdam office, bright welcoming atmosphere, teamwork and equality, 4K",
    "expat-employee-management-netherlands": "Professional photorealistic image of an international expat professional settling into their new Amsterdam office, colleagues welcoming them, world map on the wall, warm inclusive atmosphere, 4K",
    # HR S.O.S. (15)
    "dismissing-employee-netherlands-procedure": "Professional photorealistic image of a serious but professional meeting in a Dutch office, HR manager and employee across a desk with legal documents, formal atmosphere with soft lighting, gravity and professionalism, 4K",
    "emergency-dismissal-netherlands": "Professional photorealistic image of an urgent meeting in a Dutch executive office, manager reviewing critical documents marked urgent on desk, tense professional atmosphere, dramatic lighting, 4K",
    "settlement-agreement-netherlands": "Professional photorealistic image of two parties signing a formal settlement agreement document at a polished conference table, professional handshake, balanced and fair atmosphere, Dutch law books visible, 4K",
    "dutch-employment-law-urgent-questions": "Professional photorealistic image of an HR professional urgently consulting a Dutch employment lawyer via video call, laptop showing legal advisor, legal reference books open on desk, problem-solving atmosphere, 4K",
    "handling-workplace-conflict-netherlands": "Professional photorealistic image of a professional mediation session in a modern Dutch conference room, neutral mediator between two colleagues, calm de-escalation atmosphere, soft natural lighting, 4K",
    "employee-fraud-investigation-netherlands": "Professional photorealistic image of a corporate investigation file on a desk, magnifying glass over financial documents, laptop showing data analysis, professional atmosphere in a Dutch office, controlled and methodical, 4K",
    "sick-employee-not-cooperating": "Professional photorealistic image of an HR manager reviewing a complex sick leave file with concern, phone on desk showing missed calls, reintegration plan documents spread out, challenging atmosphere, 4K",
    "reorganization-crisis-netherlands": "Professional photorealistic image of a crisis management war room in a Dutch corporate office, multiple screens showing organizational charts and financial data, executive team in emergency meeting, 4K",
    "discrimination-complaint-handling": "Professional photorealistic image of a formal complaint hearing room in a Dutch office, investigator with notepad, confidential file folders, scales of justice decoration, serious and fair atmosphere, 4K",
    "works-council-dispute-resolution": "Professional photorealistic image of a negotiation between management and works council representatives in a formal Dutch meeting room, documents on table, constructive tension, professional atmosphere, 4K",
    "non-compete-enforcement-netherlands": "Professional photorealistic image of a Dutch courtroom interior, legal professionals reviewing non-compete clause documents, gavel and employment law books, formal judicial atmosphere, 4K",
    "whistleblower-protection-netherlands": "Professional photorealistic image of a confidential reporting channel setup in a modern Dutch office, secure digital reporting interface on screen, trust and protection atmosphere, privacy and security, 4K",
    "wage-claim-defense-netherlands": "Professional photorealistic image of a financial audit of payroll records in a Dutch office, calculator, payslips, and employment contract spread on desk, HR professional reviewing calculations precisely, 4K",
    "data-breach-employee-data-netherlands": "Professional photorealistic image of a cybersecurity incident response in a Dutch office, IT professional and HR manager reviewing data breach notification on screens, GDPR compliance documents, urgent but controlled, 4K",
    "union-negotiation-crisis": "Professional photorealistic image of a CLA collective bargaining negotiation in a formal Dutch meeting room, union representatives and management across a large table, complex documents, intense but respectful, 4K",
}

def create_task(prompt):
    r = requests.post(f"{API_BASE}/api/v1/jobs/createTask", headers=HEADERS, json={
        "model": "z-image", "input": {"prompt": prompt, "aspect_ratio": "16:9"}
    })
    d = r.json()
    return d.get("data", {}).get("taskId")

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
            print(f"    FAILED: {d.get('failMsg', 'unknown')}")
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
    slugs = list(PROMPTS.keys())
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    total = len(slugs)
    
    print(f"\n🎨 Generating {total - start} images via Kie.ai...\n")
    
    batch = 5
    for bs in range(start, total, batch):
        be = min(bs + batch, total)
        tasks = {}
        
        for i in range(bs, be):
            slug = slugs[i]
            fn = f"hero-{slug}.png"
            if fn in existing:
                print(f"  ✅ [{i+1}/{total}] {slug} — exists, skip")
                continue
            print(f"  🚀 [{i+1}/{total}] {slug}")
            tid = create_task(PROMPTS[slug])
            if tid:
                tasks[slug] = tid
            time.sleep(0.5)
        
        for slug, tid in tasks.items():
            idx = slugs.index(slug) + 1
            print(f"  ⏳ [{idx}/{total}] Polling {slug}...")
            urls = poll_task(tid)
            if urls:
                fp = os.path.join(OUTPUT_DIR, f"hero-{slug}.png")
                if download(urls[0], fp):
                    kb = os.path.getsize(fp) // 1024
                    print(f"  ✅ [{idx}/{total}] hero-{slug}.png ({kb} KB)")
                else:
                    print(f"  ❌ [{idx}/{total}] Download failed")
            else:
                print(f"  ❌ [{idx}/{total}] No result for {slug}")
        
        if be < total:
            print(f"\n  --- Batch done, next... ---\n")
            time.sleep(1)
    
    done = len([f for f in os.listdir(OUTPUT_DIR) if f.startswith("hero-")])
    print(f"\n🎉 {done}/{total} images ready in {OUTPUT_DIR}\n")

if __name__ == "__main__":
    main()
