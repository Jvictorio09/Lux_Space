from django.core.management.base import BaseCommand

from myApp.models import Project, ProjectImage, Service


class Command(BaseCommand):
    help = "Seed initial services and projects so the LuxSpace site looks rich on first run."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Seeding LuxSpace demo content"))

        # --- Services ---
        services_data = [
            {
                "name": "Landscaping",
                "slug": "landscaping",
                "short_label": "LANDSCAPING",
                "order_label": "01",
                "hero_kicker": "SERVICE 01",
                "hero_eyebrow": "EST. 2013",
                "hero_title": "Ready to Transform Your Landscape?",
                "hero_emphasis": "Landscape",
                "hero_intro": (
                    "Every extraordinary garden begins with a conversation. "
                    "Tell us about your land and your vision."
                ),
                "hero_background_image": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1920&q=85",
                "overview_heading": "Where Nature Becomes Art",
                "overview_body_primary": (
                    "We believe outdoor spaces deserve the same meticulous consideration as any fine interior. "
                    "Our landscaping philosophy begins not with plants and paving, but with a deep understanding "
                    "of how you wish to live."
                ),
                "overview_body_secondary": (
                    "Every project is a collaboration between our horticultural specialists, landscape architects, "
                    "and master craftsmen. The result is an environment that feels both inevitable and extraordinary."
                ),
                "display_order": 1,
            },
            {
                "name": "Interior Design",
                "slug": "interior-design",
                "short_label": "INTERIOR",
                "order_label": "02",
                "hero_title": "Interior spaces that truly live.",
                "hero_intro": "Tailored interiors crafted around how you move, gather, and rest.",
                "hero_background_image": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600&q=85",
                "display_order": 2,
            },
            {
                "name": "Renovation",
                "slug": "renovation",
                "short_label": "RENOVATION",
                "order_label": "03",
                "hero_title": "Reimagining the familiar.",
                "hero_intro": "Sensitive renovations that respect character while upgrading performance and comfort.",
                "hero_background_image": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1600&q=85",
                "display_order": 3,
            },
            {
                "name": "Design & Fitout",
                "slug": "design-fitout",
                "short_label": "FITOUT",
                "order_label": "04",
                "hero_title": "Concept to completion.",
                "hero_intro": "A single team from first sketch to final handover.",
                "hero_background_image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1600&q=85",
                "display_order": 4,
            },
            {
                "name": "Outdoor Works",
                "slug": "outdoor-works",
                "short_label": "OUTDOOR",
                "order_label": "05",
                "hero_title": "Life between inside and out.",
                "hero_intro": "Pools, pavilions and outdoor rooms that work year-round.",
                "hero_background_image": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1600&q=85",
                "display_order": 5,
            },
            {
                "name": "Joinery",
                "slug": "joinery",
                "short_label": "JOINERY",
                "order_label": "06",
                "hero_title": "Joinery with a jeweller's eye.",
                "hero_intro": "Bespoke cabinetry and millwork crafted with precision and pride.",
                "hero_background_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1600&q=85",
                "display_order": 6,
            },
        ]

        services_by_slug = {}
        for data in services_data:
            obj, created = Service.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            services_by_slug[obj.slug] = obj
            msg = "Created" if created else "Updated"
            self.stdout.write(f"  {msg} service: {obj.name}")

        # Get service references
        landscaping = services_by_slug["landscaping"]
        interior = services_by_slug["interior-design"]
        renovation = services_by_slug["renovation"]
        fitout = services_by_slug["design-fitout"]
        outdoor = services_by_slug["outdoor-works"]
        joinery = services_by_slug["joinery"]

        # --- Projects ---
        projects_data = [
            # Landscaping Projects
            {
                "service": landscaping,
                "title": "Burrawang Estate — Full Grounds",
                "slug": "burrawang-estate",
                "location": "Bowral, NSW",
                "year": "2024",
                "summary": (
                    "Our most ambitious residential commission to date — 8 hectares of sweeping country "
                    "estate transformed into formal gardens, woodland walks, kitchen gardens and water features."
                ),
                "description": (
                    "A long-form case study describing the brief, constraints, design response and "
                    "construction journey. This project represents our most comprehensive landscape transformation, "
                    "integrating formal European garden design with native Australian plantings."
                ),
                "hero_image": "https://images.unsplash.com/photo-1558905585-72ab71d1f56c?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1558905585-72ab71d1f56c?w=1200&q=85",
                "is_featured": True,
                "display_order": 1,
            },
            {
                "service": landscaping,
                "title": "Coastal Garden Retreat",
                "slug": "coastal-garden-retreat",
                "location": "Byron Bay, NSW",
                "year": "2023",
                "summary": (
                    "A sustainable coastal garden designed to thrive in salt-laden winds, featuring native "
                    "dune vegetation and protected microclimates for exotic specimens."
                ),
                "description": (
                    "This coastal property required careful plant selection and wind protection strategies. "
                    "We created distinct garden zones that transition from hardy coastal natives at the perimeter "
                    "to more delicate plantings in protected courtyards."
                ),
                "hero_image": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1200&q=85",
                "is_featured": False,
                "display_order": 2,
            },
            {
                "service": landscaping,
                "title": "Urban Rooftop Oasis",
                "slug": "urban-rooftop-oasis",
                "location": "Sydney, NSW",
                "year": "2024",
                "summary": (
                    "A sophisticated rooftop garden in the heart of Sydney, combining entertainment spaces "
                    "with lush plantings and city views."
                ),
                "description": (
                    "Transforming a bare rooftop into a multi-functional outdoor space required careful "
                    "structural planning and lightweight planting solutions. The result is a seamless "
                    "extension of the interior living space."
                ),
                "hero_image": "https://images.unsplash.com/photo-1588167056547-c183313da396?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1588167056547-c183313da396?w=1200&q=85",
                "is_featured": False,
                "display_order": 3,
            },
            # Interior Design Projects
            {
                "service": interior,
                "title": "Heritage Apartment Restoration",
                "slug": "heritage-apartment-restoration",
                "location": "Paddington, NSW",
                "year": "2024",
                "summary": (
                    "Sensitive restoration of a 1920s apartment, preserving original features while "
                    "introducing contemporary comfort and functionality."
                ),
                "description": (
                    "This project required balancing heritage conservation with modern living requirements. "
                    "We restored original cornices, fireplaces, and timber floors while integrating contemporary "
                    "kitchen and bathroom facilities."
                ),
                "hero_image": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1200&q=85",
                "is_featured": True,
                "display_order": 1,
            },
            {
                "service": interior,
                "title": "Minimalist Family Home",
                "slug": "minimalist-family-home",
                "location": "Mosman, NSW",
                "year": "2023",
                "summary": (
                    "A light-filled family home designed around simplicity and functionality, with "
                    "carefully curated spaces for work, play, and rest."
                ),
                "description": (
                    "This project demonstrates how minimalism can accommodate family life. We created "
                    "flexible spaces that adapt to different activities while maintaining a calm, uncluttered aesthetic."
                ),
                "hero_image": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200&q=85",
                "is_featured": False,
                "display_order": 2,
            },
            # Renovation Projects
            {
                "service": renovation,
                "title": "Victorian Terrace Transformation",
                "slug": "victorian-terrace-transformation",
                "location": "Surry Hills, NSW",
                "year": "2024",
                "summary": (
                    "Complete renovation of a narrow Victorian terrace, opening it to light and creating "
                    "seamless indoor-outdoor connections."
                ),
                "description": (
                    "This renovation involved structural work to open the rear of the property, creating "
                    "a light-filled extension that connects to a new courtyard garden. Original front rooms "
                    "were carefully restored."
                ),
                "hero_image": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1200&q=85",
                "is_featured": True,
                "display_order": 1,
            },
            {
                "service": renovation,
                "title": "Beach House Modernisation",
                "slug": "beach-house-modernisation",
                "location": "Newport, NSW",
                "year": "2023",
                "summary": (
                    "Updating a 1980s beach house with contemporary finishes while preserving its "
                    "relaxed coastal character."
                ),
                "description": (
                    "This renovation focused on improving energy efficiency and updating finishes while "
                    "maintaining the casual, beachside atmosphere. New windows, insulation, and sustainable "
                    "materials were key."
                ),
                "hero_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1200&q=85",
                "is_featured": False,
                "display_order": 2,
            },
            # Design & Fitout Projects
            {
                "service": fitout,
                "title": "Boutique Retail Space",
                "slug": "boutique-retail-space",
                "location": "Bondi Junction, NSW",
                "year": "2024",
                "summary": (
                    "Complete fitout of a luxury fashion boutique, creating an immersive brand experience "
                    "through thoughtful spatial design."
                ),
                "description": (
                    "This commercial fitout required careful consideration of customer flow, product display, "
                    "and brand identity. Custom joinery and lighting create distinct zones within the compact space."
                ),
                "hero_image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?w=1200&q=85",
                "is_featured": False,
                "display_order": 1,
            },
            {
                "service": fitout,
                "title": "Corporate Office Fitout",
                "slug": "corporate-office-fitout",
                "location": "Barangaroo, NSW",
                "year": "2024",
                "summary": (
                    "Modern office fitout designed to support collaboration and wellbeing, with flexible "
                    "workspaces and breakout areas."
                ),
                "description": (
                    "This project transformed a shell space into a dynamic workplace. We created a mix of "
                    "open plan areas, private offices, meeting rooms, and wellness spaces to support diverse "
                    "work styles."
                ),
                "hero_image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&q=85",
                "is_featured": True,
                "display_order": 2,
            },
            # Outdoor Works Projects
            {
                "service": outdoor,
                "title": "Infinity Pool & Pavilion",
                "slug": "infinity-pool-pavilion",
                "location": "Palm Beach, NSW",
                "year": "2024",
                "summary": (
                    "A dramatic infinity pool with integrated outdoor pavilion, creating a year-round "
                    "entertainment space with ocean views."
                ),
                "description": (
                    "This project required careful engineering to create a cantilevered pool structure "
                    "with integrated pavilion. The design maximizes views while providing shelter from "
                    "coastal winds."
                ),
                "hero_image": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1613545325278-f24b0cae1224?w=1200&q=85",
                "is_featured": True,
                "display_order": 1,
            },
            {
                "service": outdoor,
                "title": "Outdoor Kitchen & Dining",
                "slug": "outdoor-kitchen-dining",
                "location": "Vaucluse, NSW",
                "year": "2023",
                "summary": (
                    "A fully equipped outdoor kitchen and dining area, seamlessly integrated with the "
                    "landscape and pool area."
                ),
                "description": (
                    "This outdoor space functions as a complete kitchen and dining area, with built-in "
                    "BBQ, pizza oven, refrigeration, and weatherproof storage. The design creates a "
                    "seamless flow between indoor and outdoor living."
                ),
                "hero_image": "https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1600607687644-c7171b42498b?w=1200&q=85",
                "is_featured": False,
                "display_order": 2,
            },
            # Joinery Projects
            {
                "service": joinery,
                "title": "Custom Library & Study",
                "slug": "custom-library-study",
                "location": "Point Piper, NSW",
                "year": "2024",
                "summary": (
                    "Bespoke joinery creating a sophisticated library and study space, with integrated "
                    "storage and display systems."
                ),
                "description": (
                    "This project showcases our joinery craftsmanship with floor-to-ceiling bookcases, "
                    "concealed storage, and a custom desk unit. Traditional techniques were combined "
                    "with modern functionality."
                ),
                "hero_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=1200&q=85",
                "is_featured": False,
                "display_order": 1,
            },
            {
                "service": joinery,
                "title": "Kitchen Cabinetry Suite",
                "slug": "kitchen-cabinetry-suite",
                "location": "Double Bay, NSW",
                "year": "2024",
                "summary": (
                    "Complete custom kitchen with integrated appliances, pantry systems, and breakfast "
                    "nook joinery."
                ),
                "description": (
                    "This kitchen demonstrates our ability to create seamless, functional joinery that "
                    "integrates appliances and maximizes storage. The design includes a hidden pantry "
                    "system and custom breakfast nook."
                ),
                "hero_image": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=1600&q=85",
                "thumbnail_image": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?w=1200&q=85",
                "is_featured": True,
                "display_order": 2,
            },
        ]

        Project.objects.all().delete()
        ProjectImage.objects.all().delete()
        self.stdout.write("  Cleared existing projects and images")

        # Create projects
        projects_by_slug = {}
        for pdata in projects_data:
            project, created = Project.objects.update_or_create(
                slug=pdata["slug"],
                defaults=pdata,
            )
            projects_by_slug[project.slug] = project
            msg = "Created" if created else "Updated"
            self.stdout.write(f"  {msg} project: {project.title} ({project.service.name})")

        # Add gallery images for featured projects
        gallery_images = [
            {
                "project_slug": "burrawang-estate",
                "images": [
                    {"url": "https://images.unsplash.com/photo-1558905585-72ab71d1f56c?w=1600&q=85", "caption": "Formal garden approach", "is_hero": True},
                    {"url": "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=1600&q=85", "caption": "Woodland walk"},
                    {"url": "https://images.unsplash.com/photo-1588167056547-c183313da396?w=1600&q=85", "caption": "Kitchen garden"},
                    {"url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=1600&q=85", "caption": "Rose garden detail"},
                ]
            },
            {
                "project_slug": "heritage-apartment-restoration",
                "images": [
                    {"url": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600&q=85", "caption": "Restored living room", "is_hero": True},
                    {"url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1600&q=85", "caption": "Modern kitchen integration"},
                ]
            },
            {
                "project_slug": "victorian-terrace-transformation",
                "images": [
                    {"url": "https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1600&q=85", "caption": "Rear extension", "is_hero": True},
                    {"url": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=85", "caption": "Open plan living"},
                ]
            },
        ]

        for gallery_data in gallery_images:
            project_slug = gallery_data["project_slug"]
            if project_slug in projects_by_slug:
                project = projects_by_slug[project_slug]
                for idx, img_data in enumerate(gallery_data["images"], start=1):
                    ProjectImage.objects.create(
                        project=project,
                        image_url=img_data["url"],
                        caption=img_data.get("caption", ""),
                        is_hero=img_data.get("is_hero", False),
                        display_order=idx,
                    )
                self.stdout.write(f"  Added {len(gallery_data['images'])} images to {project.title}")

        self.stdout.write(self.style.SUCCESS("Seeding complete."))


