"""
Seed data for services. Edit this file to add or update services.

FORMAT (matches /services/<slug>/ layout):
  Hero:
    hero_kicker      → "SERVICE 01"
    hero_eyebrow     → "EST. 2013"
    name             → Service name
    hero_title       → Main service headline
    hero_emphasis    → Optional emphasis word fragment for stylised heading
    hero_intro       → Subtitle under heading
    cta_primary_label   → "EXPLORE SERVICE"
    cta_secondary_label → "REQUEST QUOTE"
    hero_background_image → Hero bg URL

  Overview (OUR APPROACH):
    overview_heading         → Section heading
    overview_body_primary    → First paragraph
    overview_body_secondary  → Second paragraph

  CTA section (bottom):
    cta_heading → Strong conversion headline
    cta_intro   → Supporting CTA text

  Other sections (capabilities, stats, process, testimonials) are per-template
  for now — extend Service model with JSONField if you need per-service data.
"""

SERVICES_DATA = [
    {
        "name": "Fit-Out Services",
        "slug": "fit-out-services",
        "short_label": "FITOUT",
        "order_label": "01",
        "hero_kicker": "SERVICE 01",
        "hero_eyebrow": "INTERIOR FIT-OUT EXPERTS",
        "hero_title": "End-to-End Fit-Out, Delivered with Precision",
        "hero_emphasis": "Fit-Out",
        "hero_intro": (
            "We transform empty shells into fully realised spaces—designed, built, and delivered "
            "by one accountable team from concept to handover."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1920&q=85",
        "overview_heading": "Built Around Your Space.\nDelivered With Precision.",
        "overview_body_primary": (
            "Our fit-out service brings design, engineering, and execution into one controlled process—"
            "ensuring every detail is resolved before it reaches site."
        ),
        "overview_body_secondary": (
            "By managing everything in-house, we eliminate coordination gaps, reduce rework, and deliver "
            "spaces that are refined, functional, and ready from day one."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Ready to Transform Your Space?",
        "cta_intro": "Talk to our team about creating a space that is built properly from day one.",
        "display_order": 1,
    },
    {
        "name": "Landscaping Services",
        "slug": "landscaping-services",
        "short_label": "LANDSCAPE",
        "order_label": "02",
        "hero_kicker": "SERVICE 02",
        "hero_eyebrow": "OUTDOOR DESIGN & EXECUTION",
        "hero_title": "Landscapes Designed for Modern Outdoor Living",
        "hero_emphasis": "Landscape",
        "hero_intro": (
            "We design and build outdoor environments that balance climate, architecture, and lifestyle—"
            "from planting and lighting to full outdoor living spaces."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920&q=85",
        "overview_heading": "Beautiful Outside.\nFunctional Every Day.",
        "overview_body_primary": (
            "Our landscapes are engineered for the UAE environment—balancing heat, water efficiency, "
            "and long-term performance from the ground up."
        ),
        "overview_body_secondary": (
            "We integrate design, irrigation, lighting, and build into one system—creating outdoor spaces "
            "that are not only beautiful, but effortless to maintain."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Planning Your Outdoor Space?",
        "cta_intro": "Let’s design a landscape that performs as well as it looks.",
        "display_order": 2,
    },
    {
        "name": "Custom Joinery",
        "slug": "custom-joinery",
        "short_label": "JOINERY",
        "order_label": "03",
        "hero_kicker": "SERVICE 03",
        "hero_eyebrow": "BESPOKE WOODWORK",
        "hero_title": "Bespoke Joinery, Built with Precision",
        "hero_emphasis": "Joinery",
        "hero_intro": (
            "Custom kitchens, wardrobes, and interior elements—engineered, produced, and installed "
            "by our in-house team."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1920&q=85",
        "overview_heading": "Tailored Pieces.\nSeamless Integration.",
        "overview_body_primary": (
            "Every piece begins with technical accuracy—dimensions, tolerances, and finishes are resolved "
            "before production starts."
        ),
        "overview_body_secondary": (
            "By controlling design, fabrication, and installation, we deliver joinery that fits seamlessly, "
            "functions effortlessly, and lasts."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Looking for Custom Joinery?",
        "cta_intro": "Build pieces that fit your space perfectly—designed and made in-house.",
        "display_order": 3,
    },
    {
        "name": "Swimming Pool Contracting",
        "slug": "swimming-pool-contracting",
        "short_label": "SWIMMING",
        "order_label": "04",
        "hero_kicker": "SERVICE 04",
        "hero_eyebrow": "POOL DESIGN & BUILD",
        "hero_title": "Luxury Pools Designed as Part of the Home",
        "hero_emphasis": "Swimming",
        "hero_intro": (
            "We design and build swimming pools as integrated environments—combining structure, "
            "water systems, and outdoor living into one seamless experience."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=1920&q=85",
        "overview_heading": "Designed to Impress.\nBuilt to Perform.",
        "overview_body_primary": (
            "Our pools are engineered from the ground up—structure, waterproofing, circulation, and "
            "finishes are all designed together, not added later."
        ),
        "overview_body_secondary": (
            "We integrate pools with landscape, lighting, and outdoor features—creating spaces that "
            "are both visually striking and built for long-term performance."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Thinking of Building a Pool?",
        "cta_intro": "Let’s design a pool that elevates your entire outdoor space.",
        "display_order": 4,
    },
    {
        "name": "Approval Services",
        "slug": "approval-services",
        "short_label": "APPROVALS",
        "order_label": "05",
        "hero_kicker": "SERVICE 05",
        "hero_eyebrow": "AUTHORITY APPROVAL SUPPORT",
        "hero_title": "Authority Approvals, Handled End-to-End",
        "hero_emphasis": "Approvals",
        "hero_intro": (
            "We manage documentation, submissions, and authority coordination—ensuring faster approvals "
            "with fewer delays."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=1920&q=85",
        "overview_heading": "Right Documents.\nRight Process.",
        "overview_body_primary": (
            "Navigating approvals in Dubai requires precision. We align drawings, documents, and submissions "
            "with authority requirements from the start."
        ),
        "overview_body_secondary": (
            "With direct coordination across DDA, DM, DEWA, Trakhees, and other authorities, we reduce "
            "approval friction and keep your project moving."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Faster Project Approvals?",
        "cta_intro": "Let our team handle the process—so you can focus on delivery.",
        "display_order": 5,
    },
]