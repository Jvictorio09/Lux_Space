from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Max
from django.shortcuts import get_object_or_404, redirect, render

from .forms import GalleryUploadForm, ProjectForm, ProjectImageURLForm, ServiceForm
from .models import GalleryImage, Project, ProjectImage, Service
from .utils import smart_compress_to_bytes, generate_public_id
from django.conf import settings
from io import BytesIO
from PIL import Image
import cloudinary
import cloudinary.uploader
from cloudinary import CloudinaryImage
import re


def home(request):
    """
    Render the main LuxSpace landing page.
    """
    services_qs = Service.objects.filter(is_active=True).order_by("display_order", "name")
    landing_projects = (
        Project.objects.filter(status="published")
        .select_related("service")
        .order_by("-is_featured", "display_order", "-created_at")[:5]
    )
    return render(
        request,
        "index.html",
        {"services": services_qs, "landing_projects": landing_projects},
    )


def services(request):
    """
    Render the services overview page.
    Order matches dashboard (display_order, name).
    """
    services_qs = Service.objects.filter(is_active=True).order_by("display_order", "name")
    return render(request, "service_overview.html", {"services": services_qs})


def contact(request):
    """
    Render the contact us page.
    """
    return render(request, "contact_us.html")


def service_detail(request, slug):
    """
    Render an individual service detail page, e.g. Landscaping.
    """
    service = get_object_or_404(Service, slug=slug, is_active=True)
    services_for_tabs = Service.objects.filter(is_active=True).order_by("display_order", "name")
    projects = (
        Project.objects.filter(service=service, status="published")
        .order_by("display_order", "-created_at")
        .select_related("service")
        .prefetch_related("images")
    )
    featured_project = projects.filter(is_featured=True).first() or projects.first()
    other_services = services_for_tabs.exclude(id=service.id)[:5]
    has_testimonials = any(p.testimonial_quote for p in projects)
    context = {
        "service": service,
        "services_for_tabs": services_for_tabs,
        "projects": projects,
        "featured_project": featured_project,
        "other_services": other_services,
        "has_testimonials": has_testimonials,
    }
    return render(request, "service_detail.html", context)


def projects(request):
    """
    Render the projects/portfolio overview page.
    """
    projects_qs = (
        Project.objects.filter(status="published")
        .select_related("service")
        .order_by("display_order", "-created_at")
    )
    services_qs = Service.objects.filter(is_active=True).order_by("display_order", "name")

    # Get featured project (first featured project, or first project if none featured)
    featured_project = projects_qs.filter(is_featured=True).first()
    if not featured_project:
        featured_project = projects_qs.first()
    
    # Count projects by service - create a list of tuples for easier template access
    service_counts = []
    for service in services_qs:
        count = projects_qs.filter(service=service).count()
        service_counts.append((service, count))
    
    context = {
        "projects": projects_qs,
        "services": services_qs,
        "featured_project": featured_project,
        "service_counts": service_counts,
        "total_projects": projects_qs.count(),
    }
    return render(request, "project_page/project_overview.html", context)


def project_detail(request, slug):
    """
    Render the project detail page (e.g. Burrawang Estate).
    """
    project = get_object_or_404(
        Project.objects.select_related("service"), slug=slug, status="published"
    )
    
    # Get project images (gallery)
    project_images = project.images.all().order_by("display_order", "id")
    
    # Get related projects (same service, excluding current)
    related_projects = (
        Project.objects.filter(service=project.service, status="published")
        .exclude(id=project.id)
        .select_related("service")
        .order_by("display_order", "-created_at")[:3]
    )
    
    context = {
        "project": project,
        "project_images": project_images,
        "related_projects": related_projects,
    }
    return render(request, "project_page/project_details.html", context)


class DashboardLoginView(auth_views.LoginView):
    """
    Custom-branded login page for the LuxSpace dashboard.
    """

    template_name = "dashboard/login.html"


@login_required
def dashboard_home(request):
    """
    Simple starting point for the custom client dashboard.

    From here we'll later add links to manage services, projects, and content blocks.
    """
    service_count = Service.objects.count()
    project_count = Project.objects.count()
    featured_count = Project.objects.filter(is_featured=True).count()
    context = {
        "service_count": service_count,
        "project_count": project_count,
        "featured_count": featured_count,
    }
    return render(request, "dashboard/home.html", context)


def dashboard_logout(request):
    logout(request)
    return redirect("dashboard_login")


@login_required
def dashboard_services(request):
    services = Service.objects.order_by("display_order", "name")
    if request.method == "POST" and "reorder_ids" in request.POST:
        ids_str = request.POST.get("reorder_ids", "").strip()
        if ids_str:
            try:
                ids = [int(x.strip()) for x in ids_str.split(",") if x.strip()]
                # Assign display_order 1, 2, 3, ... in exact submitted order (so first id = 1)
                for i, pk in enumerate(ids):
                    Service.objects.filter(pk=pk).update(display_order=i + 1)
                # Any service not in the list gets a higher display_order so they appear after
                others = Service.objects.exclude(pk__in=ids).order_by("display_order", "name")
                for j, svc in enumerate(others):
                    svc.display_order = len(ids) + 1 + j
                    svc.save()
                messages.success(request, "Order saved.")
            except (ValueError, TypeError):
                messages.error(request, "Invalid order.")
        return redirect("dashboard_services")
    return render(request, "dashboard/services_list.html", {"services": services})


@login_required
def dashboard_service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("dashboard_services")
    else:
        form = ServiceForm(instance=service)
    return render(
        request,
        "dashboard/service_form.html",
        {"form": form, "service": service},
    )


@login_required
def dashboard_projects(request):
    projects = Project.objects.select_related("service").order_by(
        "service__display_order", "display_order", "title"
    )
    return render(request, "dashboard/projects_list.html", {"projects": projects})


@login_required
def dashboard_project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    gallery_images = project.images.all().order_by("display_order", "id")
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("dashboard_projects")
    else:
        form = ProjectForm(instance=project)
    return render(
        request,
        "dashboard/project_form.html",
        {"form": form, "project": project, "gallery_images": gallery_images},
    )


@login_required
def dashboard_project_gallery(request, pk):
    """Manage project gallery images: add by URL, upload files, delete."""
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all().order_by("display_order", "id")

    # Reorder: save new order (from drag-and-drop)
    if request.method == "POST" and "reorder_ids" in request.POST:
        ids_str = request.POST.get("reorder_ids", "").strip()
        if ids_str:
            try:
                ids = [int(x.strip()) for x in ids_str.split(",") if x.strip()]
                valid = project.images.filter(pk__in=ids)
                id_to_obj = {obj.pk: obj for obj in valid}
                for i, pk in enumerate(ids):
                    if pk in id_to_obj:
                        id_to_obj[pk].display_order = i + 1
                        id_to_obj[pk].save()
                messages.success(request, "Order saved.")
            except (ValueError, TypeError):
                messages.error(request, "Invalid order.")
        return redirect("dashboard_project_gallery", pk=project.pk)

    # Move image to a specific position (1-based), e.g. "Add to top 10"
    if request.method == "POST" and "move_to_position" in request.POST:
        img_id = request.POST.get("move_to_position")
        target = request.POST.get("target_position", "1")
        try:
            target_pos = max(1, min(int(target), project.images.count()))
            img = ProjectImage.objects.get(pk=img_id, project=project)
            ordered = list(project.images.order_by("display_order", "id"))
            idx = next((i for i, im in enumerate(ordered) if im.pk == int(img_id)), -1)
            if idx < 0:
                raise ProjectImage.DoesNotExist
            target_idx = target_pos - 1
            if idx != target_idx:
                # Remove img from list, insert at target
                ordered.pop(idx)
                ordered.insert(target_idx, img)
                for i, im in enumerate(ordered):
                    im.display_order = i + 1
                    im.save()
                messages.success(request, f"Moved to position #{target_pos}.")
        except (ProjectImage.DoesNotExist, ValueError, TypeError):
            messages.error(request, "Could not move image.")
        return redirect("dashboard_project_gallery", pk=project.pk)

    # Delete image
    if request.method == "POST":
        if "delete_id" in request.POST:
            img_id = request.POST.get("delete_id")
            try:
                img = ProjectImage.objects.get(pk=img_id, project=project)
                img.delete()
                messages.success(request, "Image removed.")
            except ProjectImage.DoesNotExist:
                messages.error(request, "Image not found.")
            return redirect("dashboard_project_gallery", pk=project.pk)

        # Add by URL
        url_form = ProjectImageURLForm(request.POST)
        if url_form.is_valid():
            max_order = project.images.aggregate(
                m=Max("display_order")
            ).get("m") or 0
            ProjectImage.objects.create(
                project=project,
                image_url=url_form.cleaned_data["image_url"],
                caption=url_form.cleaned_data.get("caption", ""),
                is_hero=url_form.cleaned_data.get("is_hero", False),
                display_order=max_order + 1,
            )
            messages.success(request, "Image added.")
            return redirect("dashboard_project_gallery", pk=project.pk)

        # File upload (Cloudinary)
        files = request.FILES.getlist("images")
        if files:
            cloudinary.config(
                cloud_name=settings.CLOUDINARY_CLOUD_NAME,
                api_key=settings.CLOUDINARY_API_KEY,
                api_secret=settings.CLOUDINARY_API_SECRET,
                secure=True,
            )
            max_order = project.images.aggregate(
                m=Max("display_order")
            ).get("m") or 0
            uploaded = 0
            for f in files:
                try:
                    file_size_mb = f.size / (1024 * 1024)
                    if file_size_mb > 9.3:
                        file_to_upload = smart_compress_to_bytes(f)
                    else:
                        f.seek(0)
                        file_to_upload = BytesIO(f.read())
                    public_id = generate_public_id(f.name)
                    result = cloudinary.uploader.upload(
                        file_to_upload,
                        folder="luxspace/projects",
                        public_id=public_id,
                        resource_type="image",
                        access_mode="public",
                    )
                    url = result.get("secure_url") or result.get("url")
                    if url and url.startswith("http"):
                        ProjectImage.objects.create(
                            project=project,
                            image_url=url,
                            caption="",
                            display_order=max_order + uploaded + 1,
                        )
                        uploaded += 1
                except Exception as e:
                    messages.error(request, f"Upload failed: {e}")
            if uploaded:
                messages.success(request, f"Uploaded {uploaded} image(s).")
            return redirect("dashboard_project_gallery", pk=project.pk)

    url_form = ProjectImageURLForm()
    return render(
        request,
        "dashboard/project_gallery.html",
        {"project": project, "images": images, "url_form": url_form},
    )


@login_required
def dashboard_gallery(request):
    """
    Gallery manager following Cloudinary pattern:
    
    - Accepts multiple files
    - Compresses if > 9.3MB (smart_compress_to_bytes)
    - Uploads to Cloudinary with public access
    - Generates 3 URL variants (secure_url, web_url, thumb_url)
    - Stores URLs + metadata in database (no files on server)
    """

    # Configure Cloudinary from settings if not already configured
    cloudinary.config(
        cloud_name=settings.CLOUDINARY_CLOUD_NAME,
        api_key=settings.CLOUDINARY_API_KEY,
        api_secret=settings.CLOUDINARY_API_SECRET,
        secure=True,
    )

    if request.method == "POST":
        form = GalleryUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get files from form cleaned_data (handles both single and multiple)
            files = form.cleaned_data.get("images", [])
            
            # Ensure it's a list
            if not isinstance(files, list):
                files = [files] if files else []
            
            # Also try getting from request directly as fallback
            if not files:
                files = request.FILES.getlist("images")
            
            if not files:
                messages.error(request, "No files were selected. Please choose at least one image to upload.")
                return redirect("dashboard_gallery")
            
            uploaded_count = 0
            error_count = 0
            
            for f in files:
                try:
                    # Step 1: Check file size and compress if needed (> 9.3MB)
                    file_size_mb = f.size / (1024 * 1024)
                    
                    if file_size_mb > 9.3:
                        # Compress the image
                        compressed_buffer = smart_compress_to_bytes(f)
                        file_to_upload = compressed_buffer
                    else:
                        # Use original bytes
                        f.seek(0)
                        file_to_upload = BytesIO(f.read())
                    
                    # Step 2: Generate public_id from filename
                    public_id = generate_public_id(f.name)
                    full_public_id = f"luxspace/gallery/{public_id}"
                    
                    # Step 3: Upload to Cloudinary with public access and eager transformations
                    # Note: Cloudinary doesn't accept "auto" in eager transformations
                    # We'll generate optimized URLs manually after upload
                    upload_result = cloudinary.uploader.upload(
                        file_to_upload,
                        folder="luxspace/gallery",
                        public_id=public_id,
                        resource_type="image",
                        access_mode="public",  # Critical: must be public for CDN access
                        eager=[
                            # Thumbnail version (c_fill = fill dimensions, g_face = focus on faces)
                            {
                                "width": 480,
                                "height": 320,
                                "crop": "fill",
                                "gravity": "face",
                                "quality": 80,  # Use specific quality instead of "auto"
                            },
                        ],
                    )
                    
                    # Debug: Print the full upload result to see what Cloudinary returns
                    print(f"\n=== Cloudinary Upload Result for {f.name} ===")
                    print(f"Full response keys: {list(upload_result.keys())}")
                    print(f"secure_url: {upload_result.get('secure_url')}")
                    print(f"url: {upload_result.get('url')}")
                    print(f"public_id: {upload_result.get('public_id')}")
                    print(f"eager: {upload_result.get('eager')}")
                    print("=" * 50)
                    
                    # Step 4: Extract URLs and metadata directly from Cloudinary response
                    # Cloudinary returns 'secure_url' for HTTPS URLs - this is what we want
                    secure_url = upload_result.get("secure_url")
                    if not secure_url:
                        secure_url = upload_result.get("url")  # Fallback to HTTP URL
                    
                    # Validate that we got a valid URL
                    if not secure_url or not secure_url.startswith("http"):
                        print(f"ERROR: Invalid secure_url from Cloudinary: {secure_url}")
                        print(f"Full upload_result: {upload_result}")
                        raise ValueError(f"Invalid secure_url from Cloudinary: {secure_url}")
                    
                    public_id_full = upload_result.get("public_id", full_public_id)
                    
                    # Get eager transformations (thumbnail)
                    eager = upload_result.get("eager", [])
                    
                    # For web_url, use secure_url directly from Cloudinary
                    # Cloudinary's secure_url is the correct, working URL
                    # We can add transformations (f_auto,q_auto) on-the-fly when displaying if needed
                    # But for storage, use the URL exactly as Cloudinary returns it
                    web_url = secure_url
                    
                    print(f"web_url (using secure_url): {web_url}")
                    
                    # Construct thumb_url from eager transformation or manually
                    if len(eager) >= 1:
                        # Eager transformation returns the transformed image URL
                        thumb_url = eager[0].get("secure_url") or eager[0].get("url")
                        if not thumb_url or not thumb_url.startswith("http"):
                            print(f"WARNING: Invalid thumb_url from eager: {eager[0]}")
                            thumb_url = secure_url
                    else:
                        # Construct URL manually with transformations using CloudinaryImage
                        thumb_url = CloudinaryImage(public_id_full).build_url(
                            transformation=[
                                {
                                    "width": 480,
                                    "height": 320,
                                    "crop": "fill",
                                    "gravity": "face",
                                    "quality": 80,
                                }
                            ]
                        )
                    
                    # Validate thumb_url
                    if not thumb_url or not thumb_url.startswith("http"):
                        print(f"WARNING: thumb_url invalid, using secure_url: {thumb_url}")
                        thumb_url = secure_url  # Fallback to secure_url
                    
                    # Debug: Print the URLs we're about to save
                    print(f"\n=== URLs to be saved for {f.name} ===")
                    print(f"secure_url: {secure_url}")
                    print(f"web_url: {web_url}")
                    print(f"thumb_url: {thumb_url}")
                    print("=" * 50)
                    
                    # Extract metadata
                    width = upload_result.get("width")
                    height = upload_result.get("height")
                    format_type = upload_result.get("format", "")
                    bytes_size = upload_result.get("bytes")
                    
                    # Step 5: Store in database (URLs only, no files)
                    # Final validation before saving
                    if not secure_url or not secure_url.startswith("http"):
                        raise ValueError(f"Cannot save image: secure_url is invalid: {secure_url}")
                    
                    GalleryImage.objects.create(
                        title=f.name,
                        secure_url=secure_url,
                        web_url=web_url,
                        thumb_url=thumb_url,
                        public_id=public_id_full,
                        width=width,
                        height=height,
                        format=format_type,
                        bytes=bytes_size,
                    )
                    uploaded_count += 1
                    print(f"Successfully uploaded and saved: {f.name} -> {secure_url}")
                except Exception as e:
                    # Log error and track it
                    error_count += 1
                    error_msg = str(e)
                    print(f"Error uploading {f.name}: {error_msg}")
                    messages.error(request, f"Failed to upload {f.name}: {error_msg}")
            
            # Show success/error summary
            if uploaded_count > 0:
                messages.success(request, f"Successfully uploaded {uploaded_count} image(s).")
            if error_count > 0 and uploaded_count == 0:
                messages.error(request, f"Failed to upload {error_count} image(s). Please check the errors above.")
            
            return redirect("dashboard_gallery")
        else:
            # Form validation failed
            messages.error(request, "Please correct the errors below.")
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = GalleryUploadForm()

    images = GalleryImage.objects.all()
    return render(
        request,
        "dashboard/gallery.html",
        {"form": form, "images": images},
    )