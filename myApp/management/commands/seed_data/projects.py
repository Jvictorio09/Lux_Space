"""
Seed data for projects. Edit this file to add or update projects.

Each project must have "service_slug" matching a slug in services.py.
A service can have zero projects — simply don't include any with that slug.

Optional detail page fields (sections hidden when empty):
  - pull_quote, pull_quote_author
  - challenges: [{"title": "...", "description": "..."}]
  - solutions: [{"title": "...", "description": "..."}]
  - process_phases: [{"phase_label": "PHASE 01", "duration": "...", "title": "...", "description": "...", "icon": "fa-magnifying-glass", "is_last": False}]
  - outcome_intro, outcome_stats: [{"value": "2,400", "label": "PLANTS INSTALLED"}]
  - awards: [{"name": "...", "title": "...", "organization": "...", "icon": "fa-award"}]
  - testimonial_quote, testimonial_author, testimonial_location, testimonial_avatar_url
"""

PROJECTS_DATA = [
    {
        "service_slug": "landscape-installation-maintenance",
        "title": "Landscape Works for Private Villas & Pool Areas",
        "slug": "landscape-works-private-villas-pool-areas",
        "location": "UAE",
        "year": "2025",
        "summary": (
            "Comprehensive landscape installation and maintenance works for private villas, "
            "including poolside landscaping, softscape planting, hardscape detailing, irrigation, "
            "and outdoor finishing designed for long-term beauty and performance."
        ),
        "description": (
            "This project represents a full-scope landscape works package tailored for private villa "
            "properties with integrated pool areas. The scope includes softscape installation, garden "
            "layout execution, poolside planting, paving and edging coordination, irrigation support, "
            "lighting preparation, and long-term maintenance planning. The goal was to create elegant, "
            "well-balanced outdoor spaces that feel refined, usable, and easy to maintain while enhancing "
            "overall property value and lifestyle appeal."
        ),
        "hero_image": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1600&q=85",
        "thumbnail_image": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1200&q=85",
        "is_featured": True,
        "display_order": 1,

        "pull_quote": (
            "The outdoor spaces were designed to feel clean, complete, and highly livable — "
            "from the villa garden to the poolside experience."
        ),
        "pull_quote_author": "LANDSCAPE PROJECT TEAM",

        "challenges": [
            {
                "title": "Creating a cohesive landscape across multiple villa zones",
                "description": (
                    "The site required the landscape to flow naturally between entry points, garden areas, "
                    "walkways, pool zones, and villa edges without feeling fragmented or overdesigned."
                ),
            },
            {
                "title": "Balancing aesthetics with ease of maintenance",
                "description": (
                    "The landscape needed to deliver a premium visual finish while remaining practical, "
                    "durable, and manageable for ongoing upkeep."
                ),
            },
            {
                "title": "Integrating poolside landscaping with hardscape works",
                "description": (
                    "Pool areas required careful coordination between greenery, paving, edging, drainage, "
                    "and circulation so the final result felt seamless and functional."
                ),
            },
        ],

        "solutions": [
            {
                "title": "Structured landscape zoning and site coordination",
                "description": (
                    "We planned the outdoor works in coordinated zones, allowing each villa and pool area "
                    "to have a clear visual hierarchy while still feeling part of one cohesive landscape language."
                ),
            },
            {
                "title": "Durable planting and practical material selection",
                "description": (
                    "Planting palettes and finishing elements were selected for visual impact, climate suitability, "
                    "and long-term maintainability to reduce wear and improve landscape performance."
                ),
            },
            {
                "title": "Integrated installation and maintenance planning",
                "description": (
                    "Landscape installation was carried out with future maintenance in mind, helping preserve "
                    "the look, health, and usability of the gardens and pool surroundings over time."
                ),
            },
        ],

        "process_phases": [
            {
                "phase_label": "PHASE 01",
                "duration": "SITE REVIEW & PLANNING",
                "title": "Landscape Assessment and Scope Alignment",
                "description": (
                    "We reviewed the villa exteriors, pool surroundings, circulation zones, and planting areas "
                    "to define the landscape scope, technical requirements, and desired visual direction."
                ),
                "icon": "fa-magnifying-glass",
                "is_last": False,
            },
            {
                "phase_label": "PHASE 02",
                "duration": "LAYOUT & PREPARATION",
                "title": "Ground Preparation and Landscape Coordination",
                "description": (
                    "The site was prepared for softscape and hardscape works, with coordination around levels, "
                    "edges, irrigation points, and the relationship between green areas and built elements."
                ),
                "icon": "fa-layer-group",
                "is_last": False,
            },
            {
                "phase_label": "PHASE 03",
                "duration": "INSTALLATION",
                "title": "Planting, Finishing, and Poolside Landscape Works",
                "description": (
                    "Planting, lawn installation, edging, and landscape finishing were executed across villa gardens "
                    "and pool areas to create a polished, usable, and visually balanced outdoor environment."
                ),
                "icon": "fa-seedling",
                "is_last": False,
            },
            {
                "phase_label": "PHASE 04",
                "duration": "POST-COMPLETION CARE",
                "title": "Maintenance and Ongoing Landscape Support",
                "description": (
                    "After installation, the project moved into landscape care and maintenance planning to support "
                    "healthy plant establishment, consistent presentation, and long-term outdoor quality."
                ),
                "icon": "fa-star",
                "is_last": True,
            },
        ],

        "outcome_intro": (
            "The completed landscape works gave the villas a more premium outdoor presence, improved the poolside "
            "experience, and created greener, better-structured spaces designed for both presentation and everyday use."
        ),
        "outcome_stats": [
            {"value": "VILLAS", "label": "PRIVATE RESIDENTIAL UNITS"},
            {"value": "POOL", "label": "INTEGRATED OUTDOOR ZONE"},
            {"value": "FULL", "label": "LANDSCAPE INSTALLATION"},
            {"value": "ONGOING", "label": "MAINTENANCE SUPPORT"},
        ],

        "testimonial_quote": (
            '"The landscape works brought the whole property together beautifully. The villas feel more complete, '
            'the pool areas are far more inviting, and the overall finish feels premium and well considered."'
        ),
        "testimonial_author": "PRIVATE CLIENT",
        "testimonial_location": "UAE",
        "testimonial_avatar_url": "https://randomuser.me/api/portraits/men/32.jpg",
    },
]

# Gallery images per project (project_slug -> list of {url, caption?, is_hero?})
GALLERY_IMAGES = {
    "landscape-works-private-villas-pool-areas": [
        {
            "url": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1600&q=85",
            "caption": "Poolside landscape works",
            "is_hero": True,
        },
        {
            "url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1600&q=85",
            "caption": "Villa garden detailing",
        },
        {
            "url": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1600&q=85",
            "caption": "Softscape and planting zones",
        },
        {
            "url": "https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600&q=85",
            "caption": "Landscape layout and outdoor finishing",
        },
    ],
}