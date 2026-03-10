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
        "name": "Turnkey Interior Solutions",
        "slug": "turnkey-interior-solutions",
        "short_label": "TURNKEY",
        "order_label": "01",
        "hero_kicker": "SERVICE 01",
        "hero_eyebrow": "INTERIOR FIT-OUT EXPERTS",
        "hero_title": "Turnkey Interior Solutions for Homes, Offices, and Commercial Spaces",
        "hero_emphasis": "Interior",
        "hero_intro": (
            "From concept design and space planning to fit-out, finishes, and final handover, "
            "we deliver complete turnkey interior solutions tailored for residential, retail, "
            "hospitality, and corporate environments."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1920&q=85",
        "overview_heading": "Complete Interiors.\nDesigned, Built, Delivered.",
        "overview_body_primary": (
            "Our turnkey interior solutions are built for clients who want one accountable team "
            "to manage the full journey — design development, material coordination, joinery, "
            "finishing works, MEP integration, and project execution. This creates a smoother process, "
            "better quality control, and a more efficient path from idea to completion."
        ),
        "overview_body_secondary": (
            "Whether you are furnishing a private villa, upgrading an apartment, or launching a commercial fit-out, "
            "we create interiors that are practical, elegant, and built around how people actually live and work. "
            "The result is a finished space that feels cohesive, refined, and ready from day one."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Ready for a Complete Turnkey Interior Solution?",
        "cta_intro": (
            "Let’s plan your project from design to delivery with one expert team handling every detail."
        ),
        "display_order": 1,
    },
    {
        "name": "Gypsum Ceilings & Wall Décor",
        "slug": "gypsum-ceilings-wall-decor",
        "short_label": "GYPSUM",
        "order_label": "02",
        "hero_kicker": "SERVICE 02",
        "hero_eyebrow": "CEILING & FEATURE WALL SPECIALISTS",
        "hero_title": "Gypsum Ceilings and Wall Décor That Elevate Every Interior",
        "hero_emphasis": "Décor",
        "hero_intro": (
            "Custom gypsum ceilings, bulkheads, wall panels, cornices, and decorative wall treatments "
            "crafted to add depth, definition, and a premium architectural finish."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=1920&q=85",
        "overview_heading": "Architectural Detail.\nMade Visible.",
        "overview_body_primary": (
            "Ceilings and wall features shape the visual rhythm of a room. Our gypsum ceiling and wall décor services "
            "help transform plain surfaces into structured architectural statements through recessed details, clean lines, "
            "feature forms, lighting integration, and elegant decorative treatments."
        ),
        "overview_body_secondary": (
            "From contemporary minimal ceilings to more decorative feature walls, we tailor every design to the space, "
            "the lighting plan, and the final interior style. The result is a polished environment with stronger presence, "
            "better visual hierarchy, and a more finished overall feel."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Want a More Refined Ceiling and Wall Finish?",
        "cta_intro": (
            "Let’s create gypsum ceiling and wall décor details that make your interior feel complete."
        ),
        "display_order": 2,
    },
    {
        "name": "Custom Joinery & Carpentry",
        "slug": "custom-joinery-carpentry",
        "short_label": "JOINERY",
        "order_label": "03",
        "hero_kicker": "SERVICE 03",
        "hero_eyebrow": "BESPOKE WOODWORK",
        "hero_title": "Custom Joinery and Carpentry Built for Beauty, Storage, and Function",
        "hero_emphasis": "Joinery",
        "hero_intro": (
            "Bespoke wardrobes, kitchen cabinets, vanities, wall units, doors, cladding, and fine carpentry "
            "crafted to fit your space with precision."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1920&q=85",
        "overview_heading": "Tailored Woodwork.\nBuilt to Belong.",
        "overview_body_primary": (
            "Custom joinery brings order, warmth, and value to an interior. We design and fabricate bespoke carpentry "
            "solutions that maximize space, improve usability, and create a more intentional visual finish across kitchens, "
            "bedrooms, living areas, offices, and retail environments."
        ),
        "overview_body_secondary": (
            "Every piece is developed around proportion, material choice, storage logic, and installation quality. "
            "Whether you need statement cabinetry or seamless built-ins, our joinery work is made to feel integrated, "
            "durable, and truly custom to the project."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Custom Joinery That Fits Perfectly?",
        "cta_intro": (
            "Speak with our team about bespoke carpentry solutions tailored to your layout and style."
        ),
        "display_order": 3,
    },
    {
        "name": "Painting, Flooring & Renovation",
        "slug": "painting-flooring-renovation",
        "short_label": "RENOVATION",
        "order_label": "04",
        "hero_kicker": "SERVICE 04",
        "hero_eyebrow": "FINISHING & UPGRADE WORKS",
        "hero_title": "Painting, Flooring, and Renovation Services for a Fresh New Finish",
        "hero_emphasis": "Renovation",
        "hero_intro": (
            "Interior and exterior painting, flooring installation, refurbishment, and renovation works "
            "designed to upgrade tired spaces with quality materials and professional execution."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1920&q=85",
        "overview_heading": "Refresh the Space.\nRaise the Standard.",
        "overview_body_primary": (
            "Well-executed renovation work can completely change how a property looks, feels, and performs. "
            "Our painting, flooring, and renovation services are ideal for homeowners, landlords, developers, "
            "and businesses looking to modernize interiors, restore worn areas, or prepare spaces for sale, lease, or use."
        ),
        "overview_body_secondary": (
            "We combine practical site execution with a strong eye for finish quality, ensuring each surface, material transition, "
            "and detail feels properly resolved. The result is a cleaner, brighter, more valuable space delivered with less stress."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Planning a Renovation or Interior Upgrade?",
        "cta_intro": (
            "Let’s refresh your walls, floors, and finishes with renovation work that adds visible value."
        ),
        "display_order": 4,
    },
    {
        "name": "Electrical, Plumbing & HVAC Installation",
        "slug": "electrical-plumbing-hvac-installation",
        "short_label": "MEP",
        "order_label": "05",
        "hero_kicker": "SERVICE 05",
        "hero_eyebrow": "MEP INSTALLATION SERVICES",
        "hero_title": "Electrical, Plumbing, and HVAC Installation Done Right from the Start",
        "hero_emphasis": "HVAC",
        "hero_intro": (
            "Reliable MEP solutions covering electrical systems, plumbing works, air conditioning, ventilation, "
            "and coordinated installation for residential and commercial projects."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=1920&q=85",
        "overview_heading": "Core Systems.\nCoordinated Properly.",
        "overview_body_primary": (
            "Behind every successful building is a set of systems that must work flawlessly every day. "
            "Our electrical, plumbing, and HVAC installation services are planned for safety, performance, "
            "compliance, and long-term reliability across villas, apartments, offices, restaurants, and commercial fit-outs."
        ),
        "overview_body_secondary": (
            "We coordinate technical layouts carefully with design, structure, and finishing works so the final result is not only efficient, "
            "but cleanly integrated into the space. This reduces costly rework, improves building performance, and helps deliver a more dependable project."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Reliable MEP Installation for Your Project?",
        "cta_intro": (
            "Talk to our team about electrical, plumbing, and HVAC systems designed for performance and peace of mind."
        ),
        "display_order": 5,
    },
    {
        "name": "Fire Alarm & Fire-Fighting Systems",
        "slug": "fire-alarm-fire-fighting-systems",
        "short_label": "FIRE",
        "order_label": "06",
        "hero_kicker": "SERVICE 06",
        "hero_eyebrow": "LIFE SAFETY SYSTEMS",
        "hero_title": "Fire Alarm and Fire-Fighting Systems for Safer Buildings and Better Compliance",
        "hero_emphasis": "Safety",
        "hero_intro": (
            "Integrated fire alarm, detection, suppression, and fire-fighting systems designed to protect people, "
            "property, and operations while supporting regulatory compliance."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?w=1920&q=85",
        "overview_heading": "Protection First.\nSystems You Can Trust.",
        "overview_body_primary": (
            "Fire protection is one of the most critical elements of any building. We provide fire alarm and fire-fighting system solutions "
            "that support early detection, rapid response, and stronger life-safety planning for residential developments, commercial premises, "
            "industrial spaces, and public facilities."
        ),
        "overview_body_secondary": (
            "Our approach prioritizes dependable design, proper installation, and system coordination so each component performs as intended. "
            "The result is a safer environment, improved operational readiness, and greater confidence in the overall protection strategy of the property."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Fire Protection Systems Installed Properly?",
        "cta_intro": (
            "Let’s discuss a fire alarm and fire-fighting solution tailored to your building requirements."
        ),
        "display_order": 6,
    },
    {
        "name": "Smart Home Automation",
        "slug": "smart-home-automation",
        "short_label": "SMART HOME",
        "order_label": "07",
        "hero_kicker": "SERVICE 07",
        "hero_eyebrow": "CONNECTED LIVING SOLUTIONS",
        "hero_title": "Smart Home Automation for Comfort, Security, and Modern Living",
        "hero_emphasis": "Smart",
        "hero_intro": (
            "Automated lighting, climate control, security, audio, access, and device integration "
            "designed to make homes more convenient, efficient, and future-ready."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1558002038-1055e2dae1d7?w=1920&q=85",
        "overview_heading": "Technology That\nFeels Effortless.",
        "overview_body_primary": (
            "A well-designed smart home should simplify daily life, not complicate it. Our smart home automation solutions connect lighting, "
            "temperature, entertainment, security, curtains, access control, and more into one seamless user experience."
        ),
        "overview_body_secondary": (
            "We design automation systems around the way you actually use your home, ensuring the technology feels intuitive, reliable, and worth the investment. "
            "The result is a more comfortable, secure, and efficient living environment with better control at every touchpoint."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Ready to Upgrade to a Smarter Home?",
        "cta_intro": (
            "Discover smart home automation solutions that bring convenience, control, and security together."
        ),
        "display_order": 7,
    },
    {
        "name": "Hardscape & Softscape Design",
        "slug": "hardscape-softscape-design",
        "short_label": "LANDSCAPE DESIGN",
        "order_label": "08",
        "hero_kicker": "SERVICE 08",
        "hero_eyebrow": "OUTDOOR DESIGN SERVICES",
        "hero_title": "Hardscape and Softscape Design for Elegant, Functional Outdoor Spaces",
        "hero_emphasis": "Outdoor",
        "hero_intro": (
            "Landscape design services that combine paving, pathways, retaining features, lawns, planting, "
            "and greenery into a balanced outdoor environment."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920&q=85",
        "overview_heading": "Structure and Nature.\nIn Balance.",
        "overview_body_primary": (
            "Great landscape design begins with proportion, movement, and purpose. Our hardscape and softscape design services bring together built elements "
            "such as walkways, patios, edging, and stonework with planting, lawn areas, and natural textures to create outdoor spaces that feel complete and well-composed."
        ),
        "overview_body_secondary": (
            "Whether the goal is relaxation, curb appeal, entertaining, or property enhancement, we design landscapes that are both visually strong and practically usable. "
            "The result is an exterior environment that improves daily experience and adds lasting value to the property."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Planning a New Landscape Design?",
        "cta_intro": (
            "Let’s create a hardscape and softscape design that transforms your outdoor space beautifully."
        ),
        "display_order": 8,
    },
    {
        "name": "Irrigation Systems & Lighting",
        "slug": "irrigation-systems-lighting",
        "short_label": "IRRIGATION",
        "order_label": "09",
        "hero_kicker": "SERVICE 09",
        "hero_eyebrow": "OUTDOOR SYSTEMS",
        "hero_title": "Irrigation Systems and Landscape Lighting That Keep Outdoor Spaces Performing",
        "hero_emphasis": "Lighting",
        "hero_intro": (
            "Efficient irrigation, garden watering systems, and landscape lighting solutions designed "
            "to support healthy planting, lower waste, and improve nighttime appeal."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1920&q=85",
        "overview_heading": "Performance After Dark.\nHealth Every Day.",
        "overview_body_primary": (
            "A landscape needs more than visual design to thrive. Our irrigation systems and outdoor lighting services help maintain plant health, reduce manual upkeep, "
            "and enhance the usability and appearance of exterior spaces after sunset."
        ),
        "overview_body_secondary": (
            "By combining proper water distribution with thoughtfully positioned lighting, we create outdoor environments that are more efficient, safer, and more attractive. "
            "The result is a landscape that works better throughout the day and looks stronger at night."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Smarter Irrigation and Better Outdoor Lighting?",
        "cta_intro": (
            "Talk to us about outdoor systems that improve both landscape performance and visual impact."
        ),
        "display_order": 9,
    },
    {
        "name": "Custom Pool Design & Installation",
        "slug": "custom-pool-design-installation",
        "short_label": "POOLS",
        "order_label": "10",
        "hero_kicker": "SERVICE 10",
        "hero_eyebrow": "POOL DESIGN EXPERTS",
        "hero_title": "Custom Pool Design and Installation for Luxury Outdoor Living",
        "hero_emphasis": "Pool",
        "hero_intro": (
            "Bespoke swimming pool design, construction, finishing, and installation services "
            "for private residences, hospitality spaces, and premium outdoor environments."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=1920&q=85",
        "overview_heading": "More Than a Pool.\nA Destination.",
        "overview_body_primary": (
            "A custom pool should feel like part of the architecture, not an afterthought. Our pool design and installation service focuses on proportion, experience, "
            "material quality, circulation, and integration with the wider landscape to create something visually striking and genuinely enjoyable to use."
        ),
        "overview_body_secondary": (
            "From family pools and statement water features to hospitality-ready outdoor leisure spaces, we shape pool environments around how the space should feel and function. "
            "The result is a stronger outdoor lifestyle experience and a significant enhancement to property appeal."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Thinking About a Custom Pool Project?",
        "cta_intro": (
            "Let’s design and build a pool that elevates your property and transforms outdoor living."
        ),
        "display_order": 10,
    },
    {
        "name": "Maintenance, Repair & Waterproofing",
        "slug": "maintenance-repair-waterproofing",
        "short_label": "MAINTENANCE",
        "order_label": "11",
        "hero_kicker": "SERVICE 11",
        "hero_eyebrow": "PROTECTION & UPKEEP",
        "hero_title": "Maintenance, Repair, and Waterproofing Services That Protect Your Property",
        "hero_emphasis": "Protection",
        "hero_intro": (
            "Preventive maintenance, repair works, leak treatment, and waterproofing solutions "
            "designed to preserve buildings, reduce damage, and extend asset life."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?w=1920&q=85",
        "overview_heading": "Protect the Asset.\nPrevent the Damage.",
        "overview_body_primary": (
            "Small issues become expensive problems when they are ignored. Our maintenance, repair, and waterproofing services help property owners identify weaknesses early, "
            "fix defects properly, and safeguard structures from water intrusion, deterioration, and avoidable long-term damage."
        ),
        "overview_body_secondary": (
            "Whether the issue is routine upkeep or urgent repair, we focus on practical, lasting solutions that improve durability and reduce future disruption. "
            "The result is a property that stays safer, performs better, and costs less to maintain over time."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Reliable Property Maintenance or Waterproofing?",
        "cta_intro": (
            "Get expert support to repair, protect, and preserve your building before problems grow."
        ),
        "display_order": 11,
    },
    {
        "name": "Garden Layout & Planting",
        "slug": "garden-layout-planting",
        "short_label": "GARDENS",
        "order_label": "12",
        "hero_kicker": "SERVICE 12",
        "hero_eyebrow": "GARDEN DESIGN SERVICES",
        "hero_title": "Garden Layout and Planting Design for Beautiful, Balanced Green Spaces",
        "hero_emphasis": "Garden",
        "hero_intro": (
            "Thoughtful garden planning, planting schemes, and greenery selection designed "
            "to create healthy, attractive, and site-appropriate outdoor environments."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1466692476868-aef1dfb1e735?w=1920&q=85",
        "overview_heading": "Planting with Purpose.\nBeauty with Structure.",
        "overview_body_primary": (
            "A successful garden is shaped by more than aesthetics alone. Our garden layout and planting services consider movement, sunlight, maintenance level, plant performance, "
            "seasonal character, and overall composition to create outdoor spaces that feel calm, vibrant, and well resolved."
        ),
        "overview_body_secondary": (
            "From compact residential gardens to larger estate landscapes, we design planting arrangements that suit the property and climate while delivering stronger visual impact. "
            "The result is a greener environment that feels natural, intentional, and easier to enjoy."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Ready to Plan a Better Garden Layout?",
        "cta_intro": (
            "Let’s design a garden and planting scheme that brings life, structure, and beauty to your outdoor space."
        ),
        "display_order": 12,
    },
    {
        "name": "Landscape Installation & Maintenance",
        "slug": "landscape-installation-maintenance",
        "short_label": "LANDSCAPE",
        "order_label": "13",
        "hero_kicker": "SERVICE 13",
        "hero_eyebrow": "LANDSCAPE EXECUTION & CARE",
        "hero_title": "Landscape Installation and Maintenance for Lasting Outdoor Value",
        "hero_emphasis": "Landscape",
        "hero_intro": (
            "Professional landscape installation, planting execution, lawn works, and maintenance services "
            "that keep outdoor spaces healthy, polished, and performing year-round."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1598902108854-10e335adac99?w=1920&q=85",
        "overview_heading": "Installed Properly.\nMaintained Consistently.",
        "overview_body_primary": (
            "Even the best design needs proper execution and ongoing care. Our landscape installation and maintenance services ensure outdoor spaces are built correctly, "
            "established properly, and preserved through regular upkeep, seasonal attention, and proactive landscape management."
        ),
        "overview_body_secondary": (
            "This makes a major difference in appearance, plant health, safety, and long-term property presentation. "
            "The result is an outdoor environment that continues to look refined, welcoming, and investment-worthy over time."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Landscape Installation or Ongoing Maintenance?",
        "cta_intro": (
            "Partner with a team that can build your landscape well and keep it looking its best."
        ),
        "display_order": 13,
    },
    {
        "name": "Civil Work & Structural Modifications",
        "slug": "civil-work-structural-modifications",
        "short_label": "CIVIL WORK",
        "order_label": "14",
        "hero_kicker": "SERVICE 14",
        "hero_eyebrow": "STRUCTURAL & SITE WORKS",
        "hero_title": "Civil Work and Structural Modifications for Safe, Practical Project Upgrades",
        "hero_emphasis": "Structural",
        "hero_intro": (
            "Civil works, structural changes, site preparation, and building modifications carried out "
            "with careful planning, technical coordination, and execution discipline."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1541888946425-d81bb19240f5?w=1920&q=85",
        "overview_heading": "Build on the Right\nFoundation.",
        "overview_body_primary": (
            "Some projects require more than surface-level improvement. Our civil work and structural modification services support layout changes, building alterations, "
            "site works, and construction upgrades where safety, accuracy, and technical coordination are essential."
        ),
        "overview_body_secondary": (
            "We approach these works with careful planning to reduce risk, control disruption, and align execution with the wider project scope. "
            "The result is a stronger, more functional property that is better prepared for its next stage of use."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Planning Civil Works or Structural Changes?",
        "cta_intro": (
            "Speak with us about safe, well-managed civil and structural work for your next project."
        ),
        "display_order": 14,
    },
    {
        "name": "Waterproofing & Insulation",
        "slug": "waterproofing-insulation",
        "short_label": "INSULATION",
        "order_label": "15",
        "hero_kicker": "SERVICE 15",
        "hero_eyebrow": "BUILDING PROTECTION SOLUTIONS",
        "hero_title": "Waterproofing and Insulation Services That Improve Building Performance",
        "hero_emphasis": "Insulation",
        "hero_intro": (
            "Roof waterproofing, wet-area treatment, thermal insulation, and protective systems "
            "designed to control moisture, temperature, and long-term structural wear."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?w=1920&q=85",
        "overview_heading": "Seal the Weak Points.\nStrengthen Performance.",
        "overview_body_primary": (
            "Water ingress and poor insulation can quietly undermine comfort, efficiency, and structural integrity. "
            "Our waterproofing and insulation services are designed to protect buildings from moisture damage, reduce heat transfer, and improve overall environmental performance."
        ),
        "overview_body_secondary": (
            "From roofs and terraces to walls, wet areas, and critical exposed zones, we apply targeted solutions that support longer asset life and more dependable building behavior. "
            "The result is a property that stays drier, more efficient, and more resilient through time."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Need Better Waterproofing or Insulation?",
        "cta_intro": (
            "Let’s protect your building with performance-focused solutions that reduce risk and improve comfort."
        ),
        "display_order": 15,
    },
    {
        "name": "Facility Maintenance & AMC Contracts",
        "slug": "facility-maintenance-amc-contracts",
        "short_label": "FACILITY AMC",
        "order_label": "16",
        "hero_kicker": "SERVICE 16",
        "hero_eyebrow": "ONGOING PROPERTY SUPPORT",
        "hero_title": "Facility Maintenance and AMC Contracts for Reliable Ongoing Building Care",
        "hero_emphasis": "Maintenance",
        "hero_intro": (
            "Planned facility maintenance and annual maintenance contract services that help property owners, "
            "businesses, and facilities managers keep buildings running smoothly."
        ),
        "hero_background_image": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=1920&q=85",
        "overview_heading": "Consistent Service.\nFewer Surprises.",
        "overview_body_primary": (
            "Buildings perform better when maintenance is planned, not reactive. Our facility maintenance and AMC contract services provide structured support for essential systems, "
            "routine inspections, repairs, and ongoing upkeep across residential, commercial, and mixed-use properties."
        ),
        "overview_body_secondary": (
            "This gives clients a more dependable way to manage assets, reduce downtime, and control maintenance standards over time. "
            "The result is greater operational continuity, better building condition, and a more professional maintenance strategy."
        ),
        "cta_primary_label": "EXPLORE SERVICE",
        "cta_secondary_label": "REQUEST QUOTE",
        "cta_heading": "Looking for a Trusted Facility Maintenance Partner?",
        "cta_intro": (
            "Ask about our AMC and facility maintenance solutions for consistent, long-term property support."
        ),
        "display_order": 16,
    },
]