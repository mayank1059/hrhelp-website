---
description: Deploy the HRHelp website to Cloudflare Pages
---

# Deploy to Cloudflare Pages

Run these steps in order after any code changes are complete:

// turbo-all

1. Build the static site:
```bash
cd /Users/mayanktewari/Vibe/amsterdamkids/hr/hrhelp-website && npx astro build
```

2. Deploy to Cloudflare Pages:
```bash
cd /Users/mayanktewari/Vibe/amsterdamkids/hr/hrhelp-website && npx wrangler pages deploy dist --project-name hrhelp-website
```

> **Note**: If prompted to select an account, choose "Golden Pines Headquarters".
> The production branch is "production".

3. After deployment, verify the live URL from the wrangler output and confirm the changes are visible.

## Important
**This workflow MUST be run after ANY code changes to the website.** Always deploy after making modifications.
