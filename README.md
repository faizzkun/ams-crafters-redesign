# AMS Crafters - Concept Redesign (Demo)

A complete static redesign of https://www.amscrafters.com/, built as a front-end
demo to show what the site could be. Dark premium theme, classical Greek statue
artwork, scroll animations, and every verified audit flaw fixed.

## What was fixed (vs. the live site)

- One consistent number set everywhere: 50+ happy clients, 120+ projects
  delivered, 5+ years of experience, 98% client satisfaction.
- Counters animate on scroll (they start at 0 and count up when in view).
- Solid sticky header (the original let content show through it).
- Real 404 page, plus Privacy Policy and Terms pages (the original had none).
- Footer links only to verified profiles: Instagram and Upwork.
- Contact form service dropdown lists the 11 real services; budget is in USD.
- Package typos fixed (Hover, Stationery, Customer, Signage, Deluxe, Up to,
  one spelling of Content Duplicacy Check) and no fake struck-through prices.
- Case-study pages exist for all 11 projects; only ElvenWear links to a live
  site (elvenwear.pk, the only verified live URL). No invented links.
- Team page lists the 7 real people with corrected titles (never "13 specialists").
- No "No clients to display" placeholder text anywhere.

## Structure

- `index.html`, `services.html`, `services/*.html` (11 service pages)
- `portfolio.html`, `portfolio/*.html` (11 case studies)
- `packages.html`, `story.html`, `team.html`, `careers.html`
- `contact.html`, `consultation.html`, `privacy.html`, `terms.html`, `404.html`
- `assets/css/style.css`, `assets/js/main.js`, `assets/fonts/*.woff2` (local)
- `assets/img/statue-hero.png` (blue-tinted statue, sunglasses, tablet, hero),
  `statue-purple.png` (purple statue, sunglasses, cash, results/pricing),
  `statue-red.png` (red sunglasses, phone, contact/CTA and 404),
  `statue-green.png` (statue thinking at a laptop, green rim light, story/about).
  These are new AI-generated images supplied separately; the HTML keeps the
  `<img>` references and a gradient placeholder shows if a file is missing.
  Statue images fade out at the bottom edge (CSS mask-image) with a soft glow
  behind them. No reference or example photos are used anywhere on the site.
- `sitemap.xml`, `robots.txt`, `vercel.json`

## Preview locally

```bash
cd ams-crafters-redesign
python3 -m http.server 8000
# open http://localhost:8000/
```

## Deploy (Vercel)

```bash
vercel --prod
```

Then update the domain in `sitemap.xml` and `robots.txt` if it differs from
`ams-crafters-redesign-vercel.vercel.app`.

## Notes

- Forms are front-end demos with client-side validation and a success message.
  They need a backend or form endpoint before launch.
- Package feature lists are placeholder copy for the agency to confirm.
- Testimonials use the verified quotes and names from the audit.
- Concept redesign crafted by Faizan Khan, Web Developer and AI Automation
  Specialist, https://faizankhan.pages.dev/
