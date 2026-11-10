#!/usr/bin/env python3
"""Build the AMS Crafters concept redesign as static HTML.
Run: python3 build.py   (from ~/workspace/ams-crafters-redesign/)
All content is verified audit content only. No invented metrics, links, or prices.
"""
import os
from html import escape as esc

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://ams-crafters-redesign.vercel.app"
SITE_NAME = "AMS Crafters"

# ---------------------------------------------------------------- data
SERVICES = [
    ("360-marketing", "360 Marketing", "Full-Funnel 360 Degree Digital Marketing Solutions USA",
     "One strategy, every channel. Measured, optimized and built to grow.",
     ["Integrated Strategy & Planning", "Search & Performance Marketing", "Social Media & Content",
      "Email & Automation", "Direct Outreach & Sales Enablement", "Analytics & CRO"]),
    ("website-design", "Website Design", "Award-Winning Custom Website Design & UI/UX",
     "Beautiful websites designed to convert, built to scale.",
     ["Research & UX Strategy", "UI Design & Brand Systems", "Responsive Development",
      "CMS & Ecommerce", "SEO Foundations", "Launch & Support"]),
    ("mobile-app", "App Development", "Enterprise Mobile App Development (iOS & Android)",
     "Powerful apps people love to use, for iOS, Android and the web.",
     ["Native iOS & Android", "Cross-Platform (Flutter, React Native)", "UI/UX Design",
      "API & Backend", "App Store Support", "Maintenance"]),
    ("software-development", "Software Development", "Custom Software Engineering & Cloud SaaS Platforms",
     "We build custom software that powers operations, scales teams, and delights users.",
     ["Custom Web Platforms", "SaaS Product Development", "API & Integrations",
      "Cloud & DevOps", "Dashboards & Analytics", "Enterprise Support"]),
    ("seo", "SEO", "Professional Search Engine Optimization (SEO) USA",
     "Get found. Get clicked. Get customers.",
     ["Technical SEO", "On-Page Optimization", "Content & Link Building",
      "Local SEO", "SEO Reporting", "Enterprise SEO"]),
    ("branding", "Branding", "Strategic Brand Identity & Creative Direction",
     "Brands people remember, trust, and choose.",
     ["Brand Strategy", "Logo & Identity Systems", "Brand Guidelines",
      "Naming & Messaging", "Visual Direction", "Brand Launch"]),
    ("graphic-design", "Graphic Design", "High-Impact Graphic Design & Visual Media",
     "Design that stops the scroll, tells your story, and sells.",
     ["Marketing & Social Design", "Print & Packaging", "Presentation Design",
      "Illustration & Infographics", "Ad Creatives", "Brand Templates"]),
    ("product-photography", "Product Photography", "High-End E-Commerce & Product Photography",
     "Scroll-stopping product photography that sells before a single word is read.",
     ["Studio Product Shoots", "Lifestyle & Flat-Lay", "360° & Detail Shots",
      "Editing & Retouching", "Ecommerce-Ready Delivery", "Creative Direction"]),
    ("crm-solutions", "CRM Solutions", "Smart CRM Systems & Automation Solutions",
     "A CRM that works as hard as your sales team, automated, organized, and built to close.",
     ["CRM Strategy & Setup", "Sales Pipeline Automation", "Lead Management",
      "Email & Workflow Automation", "Reporting & Dashboards", "Training & Support"]),
    ("shopify", "Shopify", "Professional Shopify & Shopify Plus Development",
     "High-converting Shopify stores, built to scale your brand.",
     ["Store Setup & Theme Design", "Custom Development", "App Integration",
      "Payment & Shipping Setup", "CRO & Speed Optimization", "Ongoing Support"]),
    ("ecommerce", "Ecommerce", "Advanced E-Commerce Platforms & Headless Commerce",
     "Ecommerce platforms engineered for speed, scale, and serious sales.",
     ["Storefront Architecture", "Headless Commerce", "Payment & Checkout",
      "Product Management", "Marketplace Integration", "Performance & CRO"]),
]
SERVICE_BY_SLUG = {s[0]: s for s in SERVICES}

PROJECTS = [
    ("rovescents", "rovescents", "business", "BUSINESS",
     "A branding case study for a fragrance label. The work covered identity, packaging direction, and a clean digital presence that lets the product speak first."),
    ("orientconsultan", "orientconsultan", "business", "BUSINESS",
     "A business consultancy that needed a clearer story online. The project focused on positioning, structure, and a website visitors can navigate in seconds."),
    ("hashmi-advertising", "Hashmi Advertising", "business", "BUSINESS",
     "A full brand refresh for an advertising business, with a sharper identity and a website that presents services without clutter."),
    ("azhar-sons", "Azhar Sons", "ecommerce", "E-COMMERCE",
     "An online store build with a simple catalog, clear categories, and a checkout flow that stays out of the customer's way."),
    ("ssfitness", "SSFITNESS", "business", "BUSINESS",
     "A gym brand that needed its online presence to match the energy of the gym floor. Branding and a website built around joining, not just browsing."),
    ("crafters", "Crafters", "marketing", "MARKETING",
     "A marketing case study built on one idea: every channel telling the same story, measured in one place."),
    ("green-development-llc", "Green Development LLC", "business", "BUSINESS",
     "A development company site built for trust. Clean project pages, clear services, and an easy way to start a conversation."),
    ("m-yousuf-sons", "M. Yousuf & Sons", "ecommerce", "E-COMMERCE",
     "A family business brought online with a storefront that keeps the catalog organized and ordering simple."),
    ("gulishauk", "GULISHAUK", "ecommerce", "E-COMMERCE",
     "An ecommerce build completed in two weeks for client Gulfam, with a storefront designed to present products clearly and load fast."),
    ("blueiink", "BlueIink", "ecommerce", "E-COMMERCE",
     "An ecommerce case study with a focus on product presentation and a storefront that works as well on a phone as on a desktop."),
    ("elvenwear", "ElvenWear", "ecommerce", "E-COMMERCE",
     "A fashion ecommerce storefront with a clean catalog and a shopping flow built for mobile first."),
]

TESTIMONIALS = [
    ("Bhair-ul-Nisa", "CEO, Dab Leather",
     "We have been working with Digital Solutions for over 3 years now and it has been a positive experience. They are attentive, efficient, always give the best advice and always respond to queries straight away."),
    ("Shayan", "CEO, Shayan Elevation & Stone",
     "The AMS Crafters team genuinely understands our brand. Their combination of marketing and aesthetic insight gave our digital presence a sharp edge, and the results speak for themselves."),
    ("Khurram", "Business Owner, Hashmi Advertising",
     "They have brought a sharp, professional energy to our brand. The team is disciplined, creative, and consistently delivers beyond expectations."),
    ("Danish Javaid", "Business Owner, Unique Engineering",
     "They turned our complex engineering services into a clear, modern digital brand. The website and marketing work brought us more leads and stronger brand trust."),
    ("Hamza", "Business Owner, Bambino Photography",
     "Working with AMS Crafters was a turning point for us. Their design and marketing efforts brought elegance and consistency to our brand."),
    ("Amaan", "CEO, Amaan Transport",
     "AMS Crafters gave our transport business a complete digital makeover, from our website to our Google Business Profile. Now customers find us easily and trust us more."),
    ("Muhammad Kamil", "CEO, Taiba Luxury Transport",
     "Our website and social media finally reflect the premium service we offer. AMS Crafters delivered quality, speed, and professionalism in every step."),
    ("Shahzaib", "CEO, SS Fitness",
     "Our gym's online presence has never looked better. AMS Crafters built us a website and marketing system that keeps bringing in new members every month."),
]

CLIENTS = ["AMS Crafters", "SS Fitness", "ElvenWear", "Hashmi Advertising", "Bambino Photography",
           "Dab Leather", "TAIBA Transport", "Yousuf & Sons", "Green Developer", "Zaki Electronics",
           "Unique Engineering", "Shayan Elevation", "Amaan Transport"]

TEAM = [
    ("MK", "Murtuza Khan", "Co-Founder & CEO"),
    ("AR", "Abdul Rehman", "Co-Founder & Managing Director"),
    ("HG", "Hafiz Muhammad Gulfam", "COO"),
    ("HS", "Hassan Shah", "Multimedia & Business Development Officer"),
    ("HB", "Habib ur Rehman Baloch", "Graphics Designer"),
    ("AS", "Abdul Samad Khan", "Data Entry Executive"),
    ("SE", "Syed Eisha", "Data Analyst"),
]

PACKAGES = [
    ("web", "Web Design", False, [
        ("Startup", "$249", "", ["Up to 5 pages", "Mobile responsive design", "Contact form", "Basic on-page SEO", "1 revision round", "Delivery in 2 weeks"], False),
        ("Professional", "$599", "", ["Up to 10 pages", "Custom design, no templates", "Blog setup", "On-page SEO foundations", "2 revision rounds", "Delivery in 3 weeks"], True),
        ("Elite", "$999", "", ["Up to 15 pages", "Custom design and animations", "CMS training", "Speed optimization", "3 revision rounds", "Priority support"], False),
        ("Silver", "$1,599", "", ["Up to 25 pages", "Advanced animations", "Ecommerce ready", "Analytics setup", "Revisions included in scope", "Dedicated manager"], False),
        ("Business", "$2,499", "", ["Up to 40 pages", "Custom integrations", "Multilingual ready", "Advanced SEO setup", "Revisions included in scope", "Dedicated manager"], False),
        ("Custom CRM Portal", "$6,999", "", ["Custom portal and dashboards", "User roles and permissions", "API integrations", "Training and documentation", "6 months support", "Dedicated manager"], False),
    ]),
    ("logo", "Logo Design", False, [
        ("Basic Logo", "$59", "", ["1 logo concept", "PNG and JPG files", "1 revision round"], False),
        ("Logo Plus", "$120", "", ["3 logo concepts", "Source files included", "Stationery design set", "3 revision rounds"], True),
        ("Premium Logo", "$250", "", ["Concepts in scope until approved", "Full brand kit", "Stationery design set", "Social media kit", "Revisions included in scope"], False),
    ]),
    ("ecommerce", "Ecommerce", False, [
        ("Startup", "$999", "", ["Up to 20 products", "Payment setup", "Mobile responsive store", "Basic SEO", "1 revision round"], False),
        ("Professional", "$1,799", "", ["Up to 100 products", "Custom theme design", "Payment and shipping setup", "Discount codes", "2 revision rounds"], True),
        ("Elite", "$3,694", "", ["Up to 500 products", "Custom development", "Customer log-in area", "Signage and label design", "Stationery design", "3 revision rounds"], False),
        ("Silver", "$6,999", "", ["Up to 1,000 products", "Marketplace integration", "Advanced filters", "Abandoned cart recovery", "Priority support"], False),
        ("Business", "$9,999", "", ["Unlimited products", "Headless ready", "Custom checkout", "Multi-currency", "Dedicated manager"], False),
        ("Enterprise", "$15,000", "", ["Everything in Business", "Custom integrations", "Dedicated infrastructure", "12 months support", "Dedicated manager"], False),
    ]),
    ("branding", "Branding", False, [
        ("Startup Collateral", "$59", "", ["Business card design", "Letterhead design", "Envelope design"], False),
        ("Collateral Classic", "$129", "", ["Business card, letterhead, envelope", "Social media profile kit", "2 revision rounds"], False),
        ("Premium Collateral", "$199", "", ["Full stationery set", "Social media kit", "Brand color guide", "3 revision rounds"], True),
        ("Unlimited Collateral", "$249", "", ["Everything in Premium", "Unlimited stationery items in scope", "Presentation template"], False),
        ("Complete Branding Solution", "$994", "", ["Logo and identity system", "Brand guidelines", "Full stationery set", "Social media kit", "Launch support"], False),
    ]),
    ("video", "Video Animation", False, [
        ("Startup Video", "$499", "", ["Up to 30 seconds", "Script support", "Voiceover included", "1 revision round"], False),
        ("Delux Video", "$899", "", ["Up to 60 seconds", "Custom storyboard", "Professional voiceover", "Background music", "2 revision rounds"], True),
        ("Premium Video", "$1,199", "", ["Up to 90 seconds", "2D animation", "Sound design", "3 revision rounds"], False),
        ("Unlimited Video", "$1,399", "", ["Up to 2 minutes", "2D and motion graphics", "Sound design", "Revisions included in scope"], False),
        ("Business Video", "$1,799", "", ["Up to 3 minutes", "Full production", "Multiple formats", "Priority delivery"], False),
        ("Advance Video", "$2,199", "", ["Up to 5 minutes", "Full production team", "All formats", "12 months usage support"], False),
    ]),
    ("seo", "SEO", True, [
        ("Startup", "$449", "/mo", ["10 keywords", "On-page optimization", "Content duplicacy check", "Monthly report"], False),
        ("Professional", "$849", "/mo", ["25 keywords", "Content and link building", "Local SEO", "Content duplicacy check", "Monthly report"], True),
        ("Business", "$1,549", "/mo", ["50 keywords", "Technical SEO audit", "Content and link building", "Local SEO", "Bi-weekly report"], False),
        ("Enterprise", "$2,149", "/mo", ["100 keywords", "Enterprise SEO", "Dedicated strategist", "Content duplicacy check", "Weekly report"], False),
    ]),
    ("smm", "Social Media Marketing", True, [
        ("Startup", "$499", "/mo", ["8 posts per month", "2 platforms", "Basic graphics", "Monthly report"], False),
        ("Professional", "$999", "/mo", ["16 posts per month", "3 platforms", "Ad creatives", "Community replies", "Monthly report"], True),
        ("Business", "$2,500", "/mo", ["30 posts per month", "All platforms", "Paid ads management", "Dedicated manager", "Weekly report"], False),
    ]),
    ("combo", "Combo Packages", False, [
        ("Startup Combo", "$449", "", ["Logo design", "Business card and stationery", "Social media setup"], False),
        ("Professional Combo", "$999", "", ["Logo and branding", "Website up to 5 pages", "Social media setup", "Stationery design"], True),
        ("Business Combo", "$1,399", "", ["Logo and branding", "Website up to 10 pages", "Social media management", "Stationery design"], False),
        ("Advance Combo", "$1,999", "", ["Complete branding", "Ecommerce store", "SEO starter", "Social media management"], False),
        ("Enterprise Combo", "$2,999", "", ["Everything in Advance", "Custom development", "SEO and SMM", "Dedicated manager"], False),
    ]),
]

FAQS = [
    ("How does a project start?",
     "With a free consultation. You tell us about your goals, we map the scope and timeline, and you get a clear quote before any work begins."),
    ("How long does a website take?",
     "It depends on scope. A typical business website takes two to four weeks from approved design to launch, and the timeline is confirmed in writing before we start."),
    ("How much does it cost?",
     "Packages are transparent and start at $59 for logo design and $249 for a website. Custom work is quoted after a free consultation, with no hidden fees."),
    ("Do you offer revisions?",
     "Yes. Every package includes revision rounds, and the number is shown on the package. We keep working until the design matches the brief."),
    ("What happens after launch?",
     "We test everything, hand over the site, and stay available for support and maintenance. Ongoing SEO and social media plans are available monthly."),
    ("How do I get started?",
     "Book a free consultation or send a message through the contact page. We reply within 24 hours on business days."),
]

# ---------------------------------------------------------------- templates
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E"
           "%3Crect width='64' height='64' rx='14' fill='%230d1424'/%3E"
           "%3Cpath d='M32 8c4 10 14 14 14 28a14 14 0 1 1-28 0c0-6 3-10 6-14 1 4 3 6 5 7-1-7 0-15 3-21z' fill='%232e7cf6'/%3E%3C/svg%3E")
LOGO_SVG = ("<svg class=\"logo-mark\" viewBox=\"0 0 64 64\" aria-hidden=\"true\">"
            "<rect width=\"64\" height=\"64\" rx=\"14\" fill=\"#2e7cf6\"/>"
            "<path d=\"M32 10c4 10 13 13 13 26a13 13 0 1 1-26 0c0-5.5 2.8-9.2 5.5-13 .9 3.7 2.8 5.5 4.6 6.5C28.4 22.5 29 15 32 10z\" fill=\"#fff\"/></svg>")

NAV_LINKS = [("Home", "/index.html"), ("Story", "/story.html"), ("Our Team", "/team.html"),
             ("Portfolio", "/portfolio.html"), ("Packages", "/packages.html"),
             ("Careers", "/careers.html"), ("Contact", "/contact.html")]

def header(active):
    items = []
    for label, href in NAV_LINKS:
        if label == "Story":
            dd = "".join(
                '<li><a href="/services/%s.html">%s <span>Service</span></a></li>' % (s[0], esc(s[1]))
                for s in SERVICES)
            dd += '<li><a href="/services.html">View All Services <span>11 services</span></a></li>'
            items.append(
                '<li class="has-dropdown"><a href="/services.html"%s>Services</a>'
                '<ul class="dropdown">%s</ul></li>' % (' class="active"' if active == "Services" else "", dd))
            items.append('<li><a href="/story.html"%s>Story</a></li>' % (' class="active"' if active == "Story" else ""))
            continue
        items.append('<li><a href="%s"%s>%s</a></li>' % (href, ' class="active"' if active == label else "", label))
    return (
        '<header class="site-header"><div class="container header-inner">'
        '<a class="logo" href="/index.html" aria-label="AMS Crafters home">%s'
        '<span class="logo-text">AMS <b>CRAFTERS</b></span></a>' % LOGO_SVG +
        '<button class="nav-toggle" type="button" aria-label="Toggle menu" aria-expanded="false">☰</button>'
        '<nav class="main-nav" aria-label="Main navigation"><ul>%s</ul></nav>' % "".join(items) +
        '<a class="btn btn-primary btn-sm nav-cta" href="/consultation.html">Get Consultation</a>'
        '</div></header>')

def footer():
    service_links = "".join(
        '<li><a href="/services/%s.html">%s</a></li>' % (s[0], esc(s[1])) for s in SERVICES)
    return (
        '<footer class="site-footer"><div class="container"><div class="footer-grid">'
        '<div class="footer-brand"><a class="logo" href="/index.html">%s'
        '<span class="logo-text">AMS <b>CRAFTERS</b></span></a>'
        '<p>A full-service creative agency built by designers, strategists, and engineers obsessed with results. We build brands, websites, apps, and marketing that grow businesses.</p>'
        '<div class="social-row">'
        '<a href="https://www.instagram.com/amscrafters/" target="_blank" rel="noopener">Instagram</a>'
        '<a href="https://www.upwork.com/agencies/1826210660916349233/" target="_blank" rel="noopener">Upwork</a>'
        '</div></div>' % LOGO_SVG +
        '<div><h4>Services</h4><ul>%s</ul></div>' % service_links +
        '<div><h4>Company</h4><ul>'
        '<li><a href="/story.html">Our Story</a></li>'
        '<li><a href="/team.html">Our Team</a></li>'
        '<li><a href="/portfolio.html">Our Work</a></li>'
        '<li><a href="/packages.html">Packages</a></li>'
        '<li><a href="/careers.html">Careers</a></li>'
        '<li><a href="/contact.html">Contact</a></li>'
        '<li><a href="/privacy.html">Privacy Policy</a></li>'
        '<li><a href="/terms.html">Terms of Service</a></li>'
        '</ul></div>'
        '<div><h4>Get In Touch</h4><ul>'
        '<li><a href="mailto:support@amscrafters.com">support@amscrafters.com</a></li>'
        '<li><a href="tel:+19198085526">+1 (919) 808-5526</a></li>'
        '<li>421 Fayetteville St, Suite 1100, Raleigh, NC 27601, USA</li>'
        '<li>500 7th Ave, 8th Floor, New York, NY 10018, USA</li>'
        '<li>Mon-Fri, 9am - 6pm EST</li>'
        '</ul></div>'
        '</div><div class="footer-bottom">'
        '<span>© 2026 AMS Crafters. All rights reserved.</span>'
        '<span>Concept redesign crafted by Faizan Khan, Web Developer and AI Automation Specialist. '
        '<a href="https://faizankhan.pages.dev/" target="_blank" rel="noopener">faizankhan.pages.dev</a></span>'
        '</div></div></footer>')

def page(title, desc, body, active, url_path):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"UTF-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "<title>%s</title>\n<meta name=\"description\" content=\"%s\">\n"
            "<meta property=\"og:title\" content=\"%s\">\n"
            "<meta property=\"og:description\" content=\"%s\">\n"
            "<meta property=\"og:type\" content=\"website\">\n"
            "<meta property=\"og:url\" content=\"%s%s\">\n"
            "<meta property=\"og:site_name\" content=\"AMS Crafters\">\n"
            "<link rel=\"icon\" href=\"%s\">\n"
            "<link rel=\"stylesheet\" href=\"/assets/css/style.css\">\n"
            "</head>\n<body>\n%s\n<main>\n%s\n</main>\n%s\n"
            "<script src=\"/assets/js/main.js\"></script>\n</body>\n</html>\n"
            % (esc(title), esc(desc), esc(title), esc(desc), DOMAIN, url_path, FAVICON,
               header(active), body, footer()))

def stats_band():
    stats = [(50, "+", "Happy Clients"), (120, "+", "Projects Delivered"),
             (5, "+", "Years of Experience"), (98, "%", "Client Satisfaction")]
    cells = "".join(
        '<div class="stat"><div class="stat-num"><span data-target="%d" data-suffix="%s">0%s</span></div>'
        '<div class="stat-label">%s</div></div>' % (n, suf, suf, label) for n, suf, label in stats)
    return '<div class="stats-band reveal">%s</div>' % cells

def faq_section():
    items = "".join(
        '<div class="faq-item reveal"><button class="faq-q" type="button">%s</button>'
        '<div class="faq-a"><p>%s</p></div></div>' % (esc(q), esc(a)) for q, a in FAQS)
    return ('<section class="section"><div class="container"><div class="section-head center reveal">'
            '<span class="eyebrow">FAQ</span><h2>Questions, answered</h2>'
            '<p class="lead">Everything clients usually ask before starting a project with us.</p></div>'
            '<div class="faq">%s</div></div></section>' % items)

def cta_band(statue=None):
    statue_html = ""
    if statue:
        alts = {"red": "Classical Greek statue with red sunglasses holding a phone",
                "purple": "Classical Greek statue with sunglasses holding cash",
                "green": "Classical Greek statue thinking at a laptop with green rim light"}
        statue_html = ('<div class="statue-wrap tint-%s"><img class="statue-img" src="/assets/img/statue-%s.png" '
                       'alt="%s" data-statue="%s" loading="lazy"></div>' % (statue, statue, alts.get(statue, "Greek statue artwork"), statue))
    pct = "%"
    return ('<section class="section"><div class="container"><div class="cta-band reveal"><div class="cta-grid">'
            '<div><span class="eyebrow">Ready To Grow?</span>'
            '<h2>Let us build something great together.</h2>'
            '<p class="lead">Book a free strategy call and get a clear plan, a clear quote, and a team that delivers.</p>'
            '<div class="stats-band" style="margin-top:32px">'
            '<div class="stat"><div class="stat-num"><span data-target="50" data-suffix="+">0+</span></div>'
            '<div class="stat-label">Brands Launched</div></div>'
            '<div class="stat"><div class="stat-num"><span data-target="98" data-suffix="' + pct + '">0' + pct + '</span></div>'
            '<div class="stat-label">Client Retention</div></div></div>'
            '<div class="hero-actions" style="margin:32px 0 0">'
            '<a class="btn btn-gold" href="/consultation.html">Book a Free Call</a>'
            '<a class="btn btn-ghost" href="/portfolio.html">View Portfolio</a></div></div>'
            + statue_html + '</div></div></div></section>')

def process_section():
    steps = [("01", "Discover", "Deep-dive discovery",
              "We research your brand, goals, audience, and competitors to build a bulletproof strategy foundation."),
             ("02", "Design", "Pixel-perfect design",
              "Our designers craft visuals that align with your brand identity and conversion goals."),
             ("03", "Build", "Clean, scalable code",
              "Developers bring every design to life with fast, maintainable code and seamless integrations."),
             ("04", "Launch", "Ship & monitor",
              "We deploy, test, and watch closely, ensuring everything performs flawlessly from day one.")]
    cards = "".join(
        '<div class="card step reveal"><div class="step-num">%s</div><h3>%s</h3>'
        '<p><strong style="color:var(--text)">%s.</strong> %s</p></div>' % (n, t, s, d)
        for n, t, s, d in steps)
    return ('<section class="section"><div class="container"><div class="section-head reveal">'
            '<span class="eyebrow">Our Process</span><h2>How we bring your brand to life, step by step</h2>'
            '<p class="lead">A proven four-step process built to deliver results, on time, every time.</p></div>'
            '<div class="grid grid-4 steps">%s</div></div></section>' % cards)

def services_grid():
    cards = "".join(
        '<article class="card reveal"><div class="card-icon">%02d</div><h3>%s</h3><p>%s</p>'
        '<a class="card-link" href="/services/%s.html">Explore service →</a></article>'
        % (i + 1, esc(s[1]), esc(s[3]), s[0]) for i, s in enumerate(SERVICES))
    return cards

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return path

# ---------------------------------------------------------------- pages
def home_page():
    pain = ["Poor Brand Identity", "Slow Websites", "Weak Digital Presence", "Generic Designs",
            "Missed Deadlines", "Low Conversion Rates", "Unclear Strategy", "Mediocre Marketing"]
    marquee = "".join("<span>%s</span>" % p for p in pain)
    hero = (
        '<section class="hero"><div class="container"><div class="hero-grid">'
        '<div><span class="eyebrow reveal">Concept Redesign · Demo</span>'
        '<h1 class="reveal">Building Brands That <span class="accent">Stand Out</span>, '
        '<span class="accent-gold">Win Big</span>, Scale Fast</h1>'
        '<p class="lead reveal">AMS Crafters is a full-service creative agency built by designers, strategists, '
        'and engineers obsessed with results. We do not just build brands, we build businesses that grow faster and last longer.</p>'
        '<div class="hero-actions reveal">'
        '<a class="btn btn-primary" href="/consultation.html">Get Consultation</a>'
        '<a class="btn btn-ghost" href="/portfolio.html">View Portfolio</a></div>'
        '<p class="hero-note reveal">Free strategy call · Reply within 24 hours · No obligation</p></div>'
        '<div class="statue-wrap tint-hero reveal"><img class="statue-img" src="/assets/img/statue-hero.png" '
        'alt="Classical Greek statue with sunglasses holding a tablet" data-statue="hero" fetchpriority="high"></div>'
        '</div>' + stats_band() + '</div></section>')
    marquee_html = ('<div class="marquee" aria-hidden="true"><div class="marquee-track">%s%s</div></div>'
                    % (marquee, marquee))
    about = (
        '<section class="section"><div class="container"><div class="grid grid-2" style="align-items:center">'
        '<div class="reveal"><span class="eyebrow">About Us</span>'
        '<h2>Design, strategy, and engineering under one roof</h2>'
        '<p class="lead">From first idea to full-scale digital operations, every service is built to drive measurable growth. '
        'We solve business problems, not just design tasks.</p>'
        '<div class="hero-actions" style="margin-top:28px"><a class="btn btn-ghost" href="/story.html">Our Story →</a></div></div>'
        '<div class="reveal reveal-delay-1"><ul class="check-list">'
        '<li>Every idea transformed into visible business value</li>'
        '<li>Solutions built on scalable, proven technology</li>'
        '<li>Strong brands created through strategy, not guesswork</li>'
        '<li>Every campaign measured, optimized, and reported</li>'
        '</ul></div></div></div></section>')
    services = ('<section class="section" style="background:var(--bg-2)"><div class="container">'
                '<div class="section-head reveal"><span class="eyebrow">Our Services</span>'
                '<h2>What we do best</h2>'
                '<p class="lead">Eleven disciplines. One studio. All built to move your brand forward.</p></div>'
                '<div class="grid grid-3">%s</div></div></section>' % services_grid())
    trusted = ('<section class="section"><div class="container"><div class="section-head center reveal">'
               '<span class="eyebrow">Trusted By Growing Businesses</span>'
               '<h2>Brands that build with us</h2></div>'
               '<div class="wordmarks reveal">%s</div></div></section>'
               % "".join('<span class="wordmark">%s</span>' % esc(c) for c in CLIENTS))
    featured = [p for p in PROJECTS[:6]]
    proj_cards = "".join(project_card(p) for p in featured)
    portfolio = ('<section class="section" style="background:var(--bg-2)"><div class="container">'
                 '<div class="section-head reveal"><span class="eyebrow">Our Work</span>'
                 '<h2>Where ambition becomes a case study</h2>'
                 '<p class="lead">11 featured case studies from 120+ projects delivered. Bold brands, measurable work, '
                 'and a portfolio built on doing, not pitching.</p></div>'
                 '<div class="grid grid-3">%s</div>'
                 '<div style="text-align:center;margin-top:40px" class="reveal">'
                 '<a class="btn btn-primary" href="/portfolio.html">View All Work</a></div></div></section>' % proj_cards)
    slides = "".join(
        '<div class="slide%s"><div class="stars" aria-label="5 out of 5 stars">★★★★★</div>'
        '<blockquote>“%s”</blockquote><footer><strong>%s</strong> · %s</footer></div>'
        % (" active" if i == 0 else "", esc(q), esc(n), esc(r))
        for i, (n, r, q) in enumerate(TESTIMONIALS))
    testimonials = ('<section class="section"><div class="container"><div class="section-head center reveal">'
                    '<span class="eyebrow">Client Reviews</span><h2>What our clients say</h2></div>'
                    '<div class="slider reveal"><button class="slider-nav slider-prev" type="button" aria-label="Previous testimonial">‹</button>'
                    '%s<div class="slider-dots"></div>'
                    '<button class="slider-nav slider-next" type="button" aria-label="Next testimonial">›</button></div>'
                    '</div></section>' % slides)
    teaser = ('<section class="section" style="background:var(--bg-2)"><div class="container">'
              '<div class="section-head reveal"><span class="eyebrow">Pricing &amp; Packages</span>'
              '<h2>Transparent pricing for every budget</h2>'
              '<p class="lead">No hidden fees, no fake discounts. Pick a package or book a free call for a custom quote.</p></div>'
              '<div class="grid grid-3">'
              '<div class="card reveal"><span class="card-num">WEB DESIGN</span><h3>Professional</h3>'
              '<div class="package-price">$599</div><p>Our best-selling website package. Up to 10 pages, custom design, blog setup, and SEO foundations.</p>'
              '<a class="card-link" href="/packages.html">See all web packages →</a></div>'
              '<div class="card reveal reveal-delay-1"><span class="card-num">LOGO DESIGN</span><h3>Logo Plus</h3>'
              '<div class="package-price">$120</div><p>Our best-selling logo package. Three concepts, source files, and a stationery design set.</p>'
              '<a class="card-link" href="/packages.html">See all logo packages →</a></div>'
              '<div class="card reveal reveal-delay-2"><span class="card-num">SEO · MONTHLY</span><h3>Professional</h3>'
              '<div class="package-price">$849<small>/mo</small></div><p>Our best-selling SEO plan. 25 keywords, content and link building, and local SEO.</p>'
              '<a class="card-link" href="/packages.html">See all SEO plans →</a></div>'
              '</div><div style="text-align:center;margin-top:40px" class="reveal">'
              '<a class="btn btn-primary" href="/packages.html">View All 38 Packages</a></div></div></section>')
    workwith = ('<section class="section-tight"><div class="container" style="text-align:center">'
                '<p class="reveal" style="color:var(--faint);letter-spacing:0.14em;text-transform:uppercase;font-size:13px">'
                'We work with: Startups · Scale-ups · D2C Brands · SaaS · Agencies · Founders</p></div></section>')
    body = hero + marquee_html + about + process_section() + services + trusted + portfolio + testimonials + teaser + workwith + faq_section() + cta_band("red")
    return page("AMS Crafters | Top Digital Agency & 360 Marketing Studio USA",
                "AMS Crafters is a full-service creative agency for web design, app development, software, branding, SEO, and 360 marketing. 50+ happy clients, 120+ projects delivered.",
                body, "Home", "/index.html")

def project_card(p):
    slug, name, cat, label, desc = p
    return ('<article class="card project-card reveal" data-category="%s">'
            '<div class="project-thumb">%s</div>'
            '<div class="project-body"><span class="tag">%s</span><h3>%s</h3><p>%s</p>'
            '<a class="card-link" href="/portfolio/%s.html">View Case Study →</a></div></article>'
            % (cat, esc(name), label, esc(name), esc(desc), slug))

def services_page():
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Services</div>'
            '<span class="eyebrow reveal">Our Services</span>'
            '<h1 class="reveal">Everything your business needs to launch and grow</h1>'
            '<p class="lead reveal">From first idea to full-scale digital operations, every service is built to drive measurable growth. '
            'Eleven services, one team, one standard.</p></div></section>'
            '<section class="section-tight"><div class="container"><div class="grid grid-3">%s</div></div></section>'
            % services_grid()
            + '<section class="section"><div class="container"><div class="section-head reveal">'
            '<span class="eyebrow">Why Businesses Choose AMS Crafters</span><h2>Strategy first, design second, excuses never</h2></div>'
            '<div class="grid grid-2"><ul class="check-list reveal">'
            '<li>Every idea transformed into visible business value</li>'
            '<li>We launch solutions built on scalable, proven technology</li></ul>'
            '<ul class="check-list reveal reveal-delay-1">'
            '<li>Strong brands are created through strategy, not guesswork</li>'
            '<li>Every campaign is measured, optimized, and reported</li></ul></div></div></section>'
            + cta_band("purple"))
    return page("Our Services | Full-Stack Digital, Design & Marketing Solutions USA | AMS Crafters",
                "Eleven services from AMS Crafters: 360 marketing, website design, app development, software, SEO, branding, graphic design, product photography, CRM, Shopify, and ecommerce.",
                body, "Services", "/services.html")

def service_page(slug):
    slug_, name, title, intro, deliverables = SERVICE_BY_SLUG[slug]
    others = [s for s in SERVICES if s[0] != slug][:4]
    checks = "".join('<li>%s</li>' % esc(d) for d in deliverables)
    related = "".join(
        '<div class="card reveal"><h3>%s</h3><p>%s</p>'
        '<a class="card-link" href="/services/%s.html">Explore →</a></div>' % (esc(s[1]), esc(s[3]), s[0])
        for s in others)
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / <a href="/services.html">Services</a> / %s</div>'
            '<span class="eyebrow reveal">Service</span><h1 class="reveal">%s</h1>'
            '<p class="lead reveal">%s</p></div></section>'
            '<section class="section-tight"><div class="container"><div class="grid grid-2" style="align-items:start">'
            '<div class="reveal"><h2 style="font-size:32px">Everything included</h2>'
            '<ul class="check-list">%s</ul></div>'
            '<div class="card reveal reveal-delay-1"><span class="card-num">START HERE</span>'
            '<h3>Not sure where to begin?</h3>'
            '<p>Book a free strategy call. We will map the right scope for your goals and give you a clear quote before any work begins.</p>'
            '<div class="hero-actions" style="margin-top:22px">'
            '<a class="btn btn-primary" href="/consultation.html">Book Free Strategy Call</a>'
            '<a class="btn btn-ghost" href="/contact.html">Request Proposal</a></div></div>'
            '</div></div></section>'
            % (esc(name), esc(name), esc(intro), checks)
            + process_section()
            + '<section class="section"><div class="container"><div class="section-head reveal">'
            '<span class="eyebrow">Keep Exploring</span><h2>Related services</h2></div>'
            '<div class="grid grid-4">%s</div></div></section>' % related
            + cta_band(None))
    return page("%s | AMS Crafters" % title,
                "%s by AMS Crafters. %s" % (name, intro), body, "Services",
                "/services/%s.html" % slug)

def portfolio_page():
    filters = ('<div class="filters reveal">'
               '<button class="filter-btn active" type="button" data-filter="all">All</button>'
               '<button class="filter-btn" type="button" data-filter="business">Business</button>'
               '<button class="filter-btn" type="button" data-filter="ecommerce">E-Commerce</button>'
               '<button class="filter-btn" type="button" data-filter="marketing">Marketing</button></div>')
    cards = "".join(project_card(p) for p in PROJECTS)
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Portfolio</div>'
            '<span class="eyebrow reveal">Portfolio</span>'
            '<h1 class="reveal">Our Work</h1>'
            '<p class="lead reveal">Where ambition becomes a case study. Bold brands, real work, and a portfolio built on doing, not pitching.</p></div></section>'
            '<section class="section-tight"><div class="container">%s</div></section>'
            '<section class="section-tight"><div class="container">%s<div class="grid grid-3">%s</div></div></section>'
            % (stats_band(), filters, cards))
    body += cta_band("purple")
    return page("Case Studies & Work Portfolio | Top US Digital Agency | AMS Crafters",
                "11 featured case studies from 120+ projects delivered by AMS Crafters, across business, ecommerce, and marketing.",
                body, "Portfolio", "/portfolio.html")

def case_study_page(p):
    slug, name, cat, label, desc = p
    details = [("Category", label), ("Featured In", "120+ projects delivered")]
    if slug == "gulishauk":
        details = [("Client", "Gulfam"), ("Timeline", "2 Weeks"), ("Category", label)]
    if slug == "elvenwear":
        details = [("Category", label), ("Live Preview", "elvenwear.pk"), ("Featured In", "120+ projects delivered")]
    boxes = "".join('<div class="detail-box"><span>%s</span><strong>%s</strong></div>' % (esc(k), esc(v))
                    for k, v in details)
    preview = ""
    if slug == "elvenwear":
        preview = ('<p><a class="btn btn-primary" href="https://elvenwear.pk/" target="_blank" rel="noopener">'
                   'Live Preview of the Website ↗</a></p>')
    others = [x for x in PROJECTS if x[0] != slug][:3]
    more = "".join(project_card(x) for x in others)
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / <a href="/portfolio.html">Portfolio</a> / %s</div>'
            '<span class="tag reveal">%s</span><h1 class="reveal">%s</h1>'
            '<p class="lead reveal">%s</p>'
            '<div class="detail-list reveal">%s</div>%s'
            '<div class="hero-actions"><a class="btn btn-primary" href="/consultation.html">Start a Project</a>'
            '<a class="btn btn-ghost" href="/portfolio.html">Back to Portfolio</a></div>'
            '</div></section>'
            '<section class="section"><div class="container"><div class="section-head reveal">'
            '<span class="eyebrow">More Case Studies</span><h2>Keep exploring the work</h2></div>'
            '<div class="grid grid-3">%s</div></div></section>'
            % (esc(name), label, esc(name), esc(desc), boxes, preview, more))
    return page("%s Case Study | AMS Crafters" % name,
                "%s, a %s case study by AMS Crafters. %s" % (name, label.lower(), desc),
                body, "Portfolio", "/portfolio/%s.html" % slug)

def packages_page():
    tab_btns = "".join(
        '<button class="tab-btn%s" type="button" data-tab="%s" aria-selected="%s">%s</button>'
        % (" active" if i == 0 else "", t[0], "true" if i == 0 else "false", esc(t[1]))
        for i, t in enumerate(PACKAGES))
    panels = ""
    for i, (key, label, monthly, pkgs) in enumerate(PACKAGES):
        cards = ""
        for name, price, per, feats, best in pkgs:
            fl = "".join("<li>%s</li>" % esc(f) for f in feats)
            cards += ('<div class="card package-card%s reveal">%s'
                      '<span class="card-num">%s</span><h3>%s</h3>'
                      '<div class="package-price">%s<small>%s</small></div>'
                      '<ul class="check-list">%s</ul>'
                      '<a class="btn btn-primary" href="/contact.html">Buy Now</a></div>'
                      % (" best" if best else "", '<span class="badge">BEST SELLER</span>' if best else "",
                         esc(label.upper()), esc(name), price, per, fl))
        panels += ('<div class="tab-panel%s" id="tab-%s" role="tabpanel">%s</div>'
                   % (" active" if i == 0 else "", key, cards))
    body = ('<!-- Package feature lists are placeholder copy for the agency to confirm before publishing. '
            'Prices are the verified listed prices. -->\n'
            '<section class="page-hero"><div class="container"><div class="grid grid-2" style="align-items:center">'
            '<div><div class="breadcrumb"><a href="/index.html">Home</a> / Packages</div>'
            '<span class="eyebrow reveal">Pricing &amp; Packages</span>'
            '<h1 class="reveal">Transparent pricing for every business, every budget</h1>'
            '<p class="lead reveal">38 packages across 8 categories. No hidden fees and no fake discounts. '
            'Pick a package or book a free call for a custom quote.</p></div>'
            '<div class="statue-wrap tint-purple reveal"><img class="statue-img" src="/assets/img/statue-purple.png" '
            'alt="Classical Greek statue with sunglasses holding cash" data-statue="purple" loading="lazy"></div>'
            '</div></div></section>'
            '<section class="section-tight"><div class="container">'
            '<div class="tabs reveal" role="tablist">%s</div>%s'
            '<p class="price-note">Prices in USD. Monthly plans are billed per month. '
            'Package features are shown as listed, and the final scope is confirmed on consultation.</p>'
            '</div></section>' % (tab_btns, panels)
            + cta_band("red"))
    return page("Transparent Pricing & Digital Service Packages USA | AMS Crafters",
                "38 transparent packages from AMS Crafters: web design from $249, logo from $59, ecommerce from $999, SEO from $449 per month. No hidden fees.",
                body, "Packages", "/packages.html")

def story_page():
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Story</div>'
            '<span class="eyebrow reveal">Our Story · Digital Excellence Since 2020</span>'
            '<h1 class="reveal">From vision to velocity.</h1>'
            '<p class="lead reveal">Founded in 2020, AMS Crafters began as a small group of designers and developers '
            'who saw one problem in digital: brands were chasing trends instead of building foundations.</p></div></section>'
            '<section class="section-tight"><div class="container">%s</div></section>' % stats_band()
            + '<section class="section"><div class="container"><div class="grid grid-2">'
            '<div class="card reveal"><span class="card-num">MISSION</span><h3>What drives us</h3>'
            '<p>To build digital experiences that turn brands into category leaders through precision, creativity, '
            'and measurable performance, and to keep pushing every brand we touch forward.</p></div>'
            '<div class="card reveal reveal-delay-1"><span class="card-num">VISION</span><h3>Where we are headed</h3>'
            '<p>To be the force behind the brands that define the next decade, a design-led partner for teams '
            'building something worth noticing.</p></div></div></div></section>'
            '<section class="section" style="background:var(--bg-2)"><div class="container">'
            '<div class="section-head reveal"><span class="eyebrow">What Makes Us Different</span>'
            '<h2>Our values</h2></div><div class="grid grid-2">'
            '<div class="card reveal"><h3>We solve business problems, not just design tasks</h3>'
            '<p>Every pixel has a job to do. If it does not move the business forward, it does not ship.</p></div>'
            '<div class="card reveal reveal-delay-1"><h3>We listen before we build</h3>'
            '<p>Discovery comes first. We understand your customers, your market, and your goals before a single screen is drawn.</p></div>'
            '<div class="card reveal"><h3>We measure everything, we improve constantly</h3>'
            '<p>Launch is the start, not the finish. We track, learn, and refine until the numbers move.</p></div>'
            '<div class="card reveal reveal-delay-1"><h3>We treat your budget like our own</h3>'
            '<p>Transparent pricing, honest scopes, and no surprises. Your money is spent like it was ours.</p></div>'
            '</div></div></section>'
            + process_section() + cta_band("green"))
    return page("Our Story & Vision | Premier US Digital Agency | AMS Crafters",
                "Founded in 2020, AMS Crafters builds digital experiences that turn brands into category leaders through precision, creativity, and measurable performance.",
                body, "Story", "/story.html")

def team_page():
    cards = "".join(
        '<div class="card team-card reveal"><div class="avatar" aria-hidden="true">%s</div>'
        '<h3>%s</h3><div class="team-role">%s</div></div>' % (ini, esc(name), esc(role))
        for ini, name, role in TEAM)
    depts = [("Design", "Brand, Product, UI/UX, Design System"),
             ("Engineering", "Web, Mobile, Software, CMS"),
             ("Research & Data", "User Research, Data & Insights, Strategy, Copywriting"),
             ("Growth & Strategy", "Marketing, SEO, Paid Media, Business Development")]
    dept_cards = "".join(
        '<div class="card reveal"><h3>%s</h3><p>%s</p></div>' % (esc(d), esc(v)) for d, v in depts)
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Our Team</div>'
            '<span class="eyebrow reveal">Our Team</span>'
            '<h1 class="reveal">The minds behind AMS Crafters</h1>'
            '<p class="lead reveal">Meet the seven people who design, build, and grow ambitious brands, '
            'across four disciplines: Design, Engineering, Research &amp; Data, and Growth &amp; Strategy.</p></div></section>'
            '<section class="section-tight"><div class="container">%s</div></section>' % stats_band()
            + '<section class="section-tight"><div class="container"><div class="grid grid-3">%s</div></div></section>' % cards
            + '<section class="section"><div class="container"><div class="section-head reveal">'
            '<span class="eyebrow">Four Disciplines</span><h2>One team, every skill a launch needs</h2></div>'
            '<div class="grid grid-2">%s</div></div></section>' % dept_cards
            + cta_band("green"))
    return page("Meet Our Team | Designers, Engineers & Strategists USA | AMS Crafters",
                "Meet the seven people behind AMS Crafters: founders, engineers, designers, and analysts across design, engineering, research, and growth.",
                body, "Our Team", "/team.html")

def careers_page():
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Careers</div>'
            '<span class="eyebrow reveal">Careers</span>'
            '<h1 class="reveal">Build your career with us.</h1>'
            '<p class="lead reveal">One open role right now. If it sounds like you, we would love to hear from you.</p></div></section>'
            '<section class="section-tight"><div class="container"><div class="grid grid-2" style="align-items:start">'
            '<div class="card reveal"><span class="tag">FULL-TIME · NORTH KARACHI</span>'
            '<h3 style="font-size:28px">Senior Sales Executive</h3>'
            '<p>Own business development end to end: lead generation, client communication, deal closure, and CRM handling.</p>'
            '<h3 style="margin-top:24px">Who should apply</h3>'
            '<ul class="check-list"><li>At least 1 year experience</li>'
            '<li>Intermediate education</li><li>Good communication skills</li>'
            '<li>Fresh graduates and experienced candidates are encouraged to apply</li></ul>'
            '<div class="hero-actions" style="margin-top:26px">'
            '<a class="btn btn-primary" href="mailto:support@amscrafters.com?subject=Application%20-%20Senior%20Sales%20Executive">Apply Now</a></div></div>'
            '<div><div class="card reveal reveal-delay-1" style="margin-bottom:22px"><h3>Benefits</h3>'
            '<ul class="check-list"><li>Flexible working hours</li><li>Opportunities to grow &amp; learn</li>'
            '<li>Supportive &amp; creative environment</li><li>Exciting projects &amp; international clients</li></ul></div>'
            '<div class="card reveal reveal-delay-2"><h3>How to apply</h3>'
            '<p>Send your CV to <a href="mailto:support@amscrafters.com">support@amscrafters.com</a> '
            'with the subject “Application, Senior Sales Executive”. We reply to shortlisted candidates within one week.</p></div></div>'
            '</div></div></section>' + cta_band("purple"))
    return page("Careers & Opportunities | Join AMS Crafters Digital Team USA",
                "One open role at AMS Crafters: Senior Sales Executive, Full-Time, North Karachi. Apply by email.",
                body, "Careers", "/careers.html")

def service_options(selected=""):
    opts = ['<option value="" disabled%s>Select a service</option>' % (" selected" if not selected else "")]
    for s in SERVICES:
        opts.append('<option value="%s">%s</option>' % (esc(s[1]), esc(s[1])))
    opts.append('<option value="Other">Other</option>')
    return "".join(opts)

def contact_page():
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Contact</div>'
            '<span class="eyebrow reveal">Contact</span>'
            '<h1 class="reveal">Get in touch.<br>Let us build something great together.</h1></div></section>'
            '<section class="section-tight"><div class="container"><div class="grid grid-2" style="align-items:start">'
            '<div class="contact-cards reveal">'
            '<div class="contact-card"><div class="card-icon">✆</div><div><h3>Call us</h3>'
            '<p><a href="tel:+19198085526">+1 (919) 808-5526</a><br>Reach out to discuss your project.</p></div></div>'
            '<div class="contact-card"><div class="card-icon">✉</div><div><h3>Email us</h3>'
            '<p><a href="mailto:support@amscrafters.com">support@amscrafters.com</a><br>We reply within 24 hours.</p></div></div>'
            '<div class="contact-card"><div class="card-icon">⌖</div><div><h3>Raleigh office</h3>'
            '<p>421 Fayetteville St, Suite 1100, Raleigh, NC 27601, USA</p></div></div>'
            '<div class="contact-card"><div class="card-icon">⌖</div><div><h3>New York office</h3>'
            '<p>500 7th Ave, 8th Floor, New York, NY 10018, USA</p></div></div>'
            '<div class="contact-card"><div class="card-icon">◷</div><div><h3>Office hours</h3>'
            '<p>Monday to Friday, 9am to 6pm EST</p></div></div></div>'
            '<div class="form-card reveal reveal-delay-1">'
            '<!-- Forms are a front-end demo in this concept redesign and need a backend or form endpoint before launch. -->'
            '<h2 style="font-size:28px;margin-bottom:8px">Send us a message</h2>'
            '<p style="color:var(--muted);margin-bottom:24px">Tell us about your project and we will reply within 24 hours.</p>'
            '<form data-demo-form novalidate><div class="form-grid">'
            '<div class="field"><label for="c-name">Full Name <span>*</span></label>'
            '<input id="c-name" name="name" type="text" required placeholder="Your full name">'
            '<span class="field-error">Please enter your name.</span></div>'
            '<div class="field"><label for="c-email">Email Address <span>*</span></label>'
            '<input id="c-email" name="email" type="email" required placeholder="you@company.com">'
            '<span class="field-error">Please enter a valid email address.</span></div>'
            '<div class="field"><label for="c-phone">Phone <span>*</span></label>'
            '<input id="c-phone" name="phone" type="tel" required placeholder="+1 555 123 4567">'
            '<span class="field-error">Please enter your phone number.</span></div>'
            '<div class="field"><label for="c-service">Service <span>*</span></label>'
            '<select id="c-service" name="service" required>%s</select>'
            '<span class="field-error">Please choose a service.</span></div>'
            '<div class="field"><label for="c-budget">Budget (USD)</label>'
            '<select id="c-budget" name="budget"><option value="">Select a budget range</option>'
            '<option>$100 - $500</option><option>$500 - $1,000</option>'
            '<option>$1,000 - $5,000</option><option>$5,000+</option></select></div>'
            '<div class="field"><label for="c-hear">How did you hear about us?</label>'
            '<select id="c-hear" name="source"><option value="">Select an option</option>'
            '<option>Google</option><option>Social Media</option><option>Referral</option><option>Other</option></select></div>'
            '<div class="field full"><label for="c-details">Project Details <span>*</span></label>'
            '<textarea id="c-details" name="details" required placeholder="Tell us about your project, goals, and timeline."></textarea>'
            '<span class="field-error">Please tell us a little about your project.</span></div>'
            '</div><button class="btn btn-primary" type="submit" style="margin-top:24px;width:100%%">Send Message</button>'
            '<div class="form-success">Thank you. Your message has been received. We will reply within 24 hours on business days.</div>'
            '</form></div></div></div></section>'
            % service_options()
            + faq_section())
    return page("Contact AMS Crafters | Get a Free Digital Consultation USA",
                "Contact AMS Crafters: call +1 (919) 808-5526 or email support@amscrafters.com. Offices in Raleigh, NC and New York. We reply within 24 hours.",
                body, "Contact", "/contact.html")

def consultation_page():
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Consultation</div>'
            '<span class="eyebrow reveal">Free Consultation</span>'
            '<h1 class="reveal">Book Your Free Consultation</h1>'
            '<p class="lead reveal">Three simple steps: fill out the form and we will reply within 24 hours, '
            'tell us about your project and goals, and our strategists will schedule a free consultation call.</p></div></section>'
            '<section class="section-tight"><div class="container"><div class="grid grid-2" style="align-items:start">'
            '<div class="form-card reveal">'
            '<!-- Forms are a front-end demo in this concept redesign and need a backend or form endpoint before launch. -->'
            '<h2 style="font-size:28px;margin-bottom:8px">Your Idea Starts Here</h2>'
            '<p style="color:var(--muted);margin-bottom:24px">Pick a time that suits you. The call is free and there is no obligation.</p>'
            '<form data-demo-form novalidate><div class="form-grid">'
            '<div class="field"><label for="k-name">Your Name <span>*</span></label>'
            '<input id="k-name" name="name" type="text" required placeholder="Your name">'
            '<span class="field-error">Please enter your name.</span></div>'
            '<div class="field"><label for="k-email">Your Email <span>*</span></label>'
            '<input id="k-email" name="email" type="email" required placeholder="you@company.com">'
            '<span class="field-error">Please enter a valid email address.</span></div>'
            '<div class="field"><label for="k-phone">Phone <span>*</span></label>'
            '<input id="k-phone" name="phone" type="tel" required placeholder="+1 555 123 4567">'
            '<span class="field-error">Please enter your phone number.</span></div>'
            '<div class="field"><label for="k-service">Service Required <span>*</span></label>'
            '<select id="k-service" name="service" required>'
            '<option value="" disabled selected>Select a service</option>'
            '<option>Branding</option><option>UI/UX Design</option><option>Web Development</option>'
            '<option>App Development</option><option>Digital Marketing</option><option>Other</option></select>'
            '<span class="field-error">Please choose a service.</span></div>'
            '<div class="field"><label for="k-date">Preferred Meeting Date</label>'
            '<input id="k-date" name="date" type="date"></div>'
            '<div class="field"><label for="k-time">Preferred Meeting Time</label>'
            '<input id="k-time" name="time" type="time"></div>'
            '<div class="field full"><label for="k-goals">What do you want to achieve? <span>*</span></label>'
            '<textarea id="k-goals" name="goals" required placeholder="Tell us about your project, goals, and budget."></textarea>'
            '<span class="field-error">Please tell us about your goals.</span></div>'
            '</div><button class="btn btn-primary" type="submit" style="margin-top:24px;width:100%%">Send Message</button>'
            '<div class="form-success">Thank you. Your consultation request has been received. We will reply within 24 hours to confirm your call.</div>'
            '</form>'
            '<p style="color:var(--faint);font-size:13.5px;margin-top:18px">By submitting this form, you consent to receiving '
            'calls, emails, and text messages related to your request from AMS Crafters.</p></div>'
            '<div class="contact-cards reveal reveal-delay-1">'
            '<div class="contact-card"><div class="card-icon">✆</div><div><h3>Call us</h3>'
            '<p><a href="tel:+19198085526">+1 (919) 808-5526</a></p></div></div>'
            '<div class="contact-card"><div class="card-icon">✉</div><div><h3>Email us</h3>'
            '<p><a href="mailto:support@amscrafters.com">support@amscrafters.com</a></p></div></div>'
            '<div class="contact-card"><div class="card-icon">⌖</div><div><h3>Offices</h3>'
            '<p>421 Fayetteville St, Suite 1100, Raleigh, NC 27601, USA<br>'
            '500 7th Ave, 8th Floor, New York, NY 10018, USA</p></div></div>'
            '<div class="contact-card"><div class="card-icon">◷</div><div><h3>Hours</h3>'
            '<p>Monday to Friday, 9am to 6pm EST</p></div></div></div>'
            '</div></div></section>')
    return page("Book a Free Digital Strategy Consultation USA | AMS Crafters",
                "Book a free digital strategy consultation with AMS Crafters. Tell us your goals and we will schedule a free call within 24 hours.",
                body, "Contact", "/consultation.html")

def legal_page(kind):
    if kind == "privacy":
        title, desc = "Privacy Policy | AMS Crafters", "Privacy policy for amscrafters.com."
        body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
                '<a href="/index.html">Home</a> / Privacy Policy</div>'
                '<h1 class="reveal">Privacy Policy</h1>'
                '<p class="lead reveal">Last updated: 10 November 2026. This page explains what information we collect and how we use it.</p>'
                '</div></section><section class="section-tight legal"><div class="container" style="max-width:780px">'
                '<h2>Information we collect</h2>'
                '<p>When you contact us through a form, we collect the details you provide, such as your name, email address, '
                'phone number, and project details. We also collect basic, anonymous usage data that helps us improve the website.</p>'
                '<h2>How we use it</h2><ul><li>To reply to your enquiry and schedule consultations.</li>'
                '<li>To prepare quotes and deliver the services you request.</li>'
                '<li>To improve the website and our services.</li></ul>'
                '<h2>Sharing</h2><p>We do not sell your personal information. We share it only when needed to deliver a service '
                'you asked for, or when required by law.</p>'
                '<h2>Your choices</h2><p>You can ask us to correct or delete your contact details at any time by emailing '
                '<a href="mailto:support@amscrafters.com">support@amscrafters.com</a>.</p>'
                '<h2>Contact</h2><p>Questions about this policy: <a href="mailto:support@amscrafters.com">support@amscrafters.com</a>, '
                '+1 (919) 808-5526.</p></div></section>')
        return page(title, desc, body, "", "/privacy.html")
    title, desc = "Terms of Service | AMS Crafters", "Terms of service for AMS Crafters."
    body = ('<section class="page-hero"><div class="container"><div class="breadcrumb">'
            '<a href="/index.html">Home</a> / Terms of Service</div>'
            '<h1 class="reveal">Terms of Service</h1>'
            '<p class="lead reveal">Last updated: 10 November 2026. These terms cover the services listed on this website.</p>'
            '</div></section><section class="section-tight legal"><div class="container" style="max-width:780px">'
            '<h2>Services and pricing</h2><p>Package prices are shown in USD on the Packages page. The final scope, timeline, '
            'and price for any project are confirmed in writing before work begins.</p>'
            '<h2>Revisions</h2><p>Each package includes the revision rounds shown on its card. Extra revisions and out-of-scope '
            'work are quoted separately.</p>'
            '<h2>Payments</h2><p>Payment terms are agreed before work starts. Monthly plans (SEO and social media) are billed per month.</p>'
            '<h2>Intellectual property</h2><p>On full payment, the client receives the agreed deliverables. AMS Crafters may show '
            'completed work in its portfolio unless the client asks otherwise in writing.</p>'
            '<h2>Liability</h2><p>We work to the agreed scope and timeline. Liability is limited to the fees paid for the service in question.</p>'
            '<h2>Contact</h2><p>Questions about these terms: <a href="mailto:support@amscrafters.com">support@amscrafters.com</a>, '
            '+1 (919) 808-5526.</p></div></section>')
    return page(title, desc, body, "", "/terms.html")

def error_page():
    body = ('<section class="error-page"><div class="container">'
            '<div class="error-code reveal">404</div>'
            '<h1 class="reveal" style="font-size:clamp(28px,4vw,44px)">This page went the way of ancient Rome.</h1>'
            '<p class="lead reveal" style="margin:18px auto 32px">The page you are looking for does not exist, or it moved. '
            'Let us get you back on track.</p>'
            '<div class="hero-actions reveal" style="justify-content:center">'
            '<a class="btn btn-primary" href="/index.html">Go Home</a>'
            '<a class="btn btn-ghost" href="/contact.html">Contact Us</a></div>'
            '<div class="statue-wrap tint-red reveal" style="max-width:340px;margin:48px auto 0">'
            '<img class="statue-img" src="/assets/img/statue-red.png" '
            'alt="Classical Greek statue with red sunglasses holding a phone" data-statue="red" loading="lazy"></div>'
            '</div></section>')
    return page("Page Not Found | AMS Crafters",
                "The page you are looking for does not exist. Return to the AMS Crafters homepage.",
                body, "", "/404.html")

def sitemap_xml(pages):
    urls = "".join(
        '<url><loc>%s%s</loc><lastmod>2026-11-11</lastmod><changefreq>monthly</changefreq><priority>%s</priority></url>\n'
        % (DOMAIN, p, "1.0" if p == "/index.html" else "0.8") for p in pages)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)

def robots_txt():
    return "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % DOMAIN

def vercel_json():
    return '{\n  "cleanUrls": true,\n  "trailingSlash": false\n}\n'

def readme_md():
    return """# AMS Crafters — Concept Redesign (Demo)

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
- `assets/img/statue-hero.png` (blue-tinted statue, sunglasses, tablet — hero),
  `statue-purple.png` (purple statue, sunglasses, cash — results/pricing),
  `statue-red.png` (red sunglasses, phone — contact/CTA and 404),
  `statue-green.png` (statue thinking at a laptop, green rim light — story/about).
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
`ams-crafters-redesign.vercel.app`.

## Notes

- Forms are front-end demos with client-side validation and a success message.
  They need a backend or form endpoint before launch.
- Package feature lists are placeholder copy for the agency to confirm.
- Testimonials use the verified quotes and names from the audit.
- Concept redesign crafted by Faizan Khan, Web Developer and AI Automation
  Specialist — https://faizankhan.pages.dev/
"""

# ---------------------------------------------------------------- build
def main():
    built = []
    built.append(write("index.html", home_page()))
    built.append(write("services.html", services_page()))
    for slug, *_ in SERVICES:
        built.append(write("services/%s.html" % slug, service_page(slug)))
    built.append(write("portfolio.html", portfolio_page()))
    for p in PROJECTS:
        built.append(write("portfolio/%s.html" % p[0], case_study_page(p)))
    built.append(write("packages.html", packages_page()))
    built.append(write("story.html", story_page()))
    built.append(write("team.html", team_page()))
    built.append(write("careers.html", careers_page()))
    built.append(write("contact.html", contact_page()))
    built.append(write("consultation.html", consultation_page()))
    built.append(write("privacy.html", legal_page("privacy")))
    built.append(write("terms.html", legal_page("terms")))
    built.append(write("404.html", error_page()))
    pages = ["/" + b for b in built if b.endswith(".html")]
    built.append(write("sitemap.xml", sitemap_xml(pages)))
    built.append(write("robots.txt", robots_txt()))
    built.append(write("vercel.json", vercel_json()))
    built.append(write("README.md", readme_md()))
    print("Built %d files:" % len(built))
    for b in sorted(built):
        print("  " + b)

if __name__ == "__main__":
    main()
