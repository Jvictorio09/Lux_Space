from django.core.management.base import BaseCommand
from django.utils import timezone

from myApp.models import Insight, Project, ProjectImage, Service

from .seed_data.insights import INSIGHTS_DATA
from .seed_data.projects import GALLERY_IMAGES, PROJECTS_DATA
from .seed_data.services import SERVICES_DATA


class Command(BaseCommand):
    help = "Seed initial services, projects, and insights so the LuxSpace site looks rich on first run."

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING("Seeding LuxSpace demo content"))

        # --- Clear existing data (order matters: projects depend on services) ---
        ProjectImage.objects.all().delete()
        Project.objects.all().delete()
        Service.objects.all().delete()
        self.stdout.write("  Cleared existing services, projects, and images")

        # --- Services ---
        services_by_slug = {}
        for data in SERVICES_DATA:
            obj, created = Service.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            services_by_slug[obj.slug] = obj
            msg = "Created" if created else "Updated"
            self.stdout.write(f"  {msg} service: {obj.name}")

        # --- Projects ---
        for pdata in PROJECTS_DATA:
            pdata = dict(pdata)
            service_slug = pdata.pop("service_slug")
            service = services_by_slug.get(service_slug)
            if not service:
                self.stdout.write(
                    self.style.WARNING(f"  Skipping project '{pdata['slug']}': service '{service_slug}' not found")
                )
                continue

            project, created = Project.objects.update_or_create(
                slug=pdata["slug"],
                defaults={**pdata, "service": service},
            )
            msg = "Created" if created else "Updated"
            self.stdout.write(f"  {msg} project: {project.title} ({project.service.name})")

        # --- Gallery images ---
        projects_by_slug = {p.slug: p for p in Project.objects.all()}
        for project_slug, images in GALLERY_IMAGES.items():
            if project_slug in projects_by_slug:
                project = projects_by_slug[project_slug]
                for idx, img_data in enumerate(images, start=1):
                    ProjectImage.objects.create(
                        project=project,
                        image_url=img_data["url"],
                        caption=img_data.get("caption", ""),
                        is_hero=img_data.get("is_hero", False),
                        display_order=idx,
                    )
                self.stdout.write(f"  Added {len(images)} images to {project.title}")

        # --- Insights ---
        for idata in INSIGHTS_DATA:
            idata = dict(idata)
            obj, created = Insight.objects.update_or_create(
                slug=idata["slug"],
                defaults={
                    **idata,
                    "published_at": timezone.now() if idata.get("status") == "published" else None,
                },
            )
            msg = "Created" if created else "Updated"
            self.stdout.write(f"  {msg} insight: {obj.title}")

        self.stdout.write(self.style.SUCCESS("Seeding complete."))
