from django.contrib import admin

from .models import GalleryImage, Project, ProjectImage, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "short_label", "order_label", "is_active", "display_order")
    list_editable = ("is_active", "display_order")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "short_label")
    ordering = ("display_order", "name")


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "service", "location", "year", "is_featured", "status")
    list_filter = ("service", "status", "is_featured")
    list_editable = ("is_featured", "status")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "location", "summary")
    inlines = [ProjectImageInline]


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "secure_url", "width", "height", "format", "created_at")
    list_filter = ("format", "created_at")
    search_fields = ("title", "public_id")
    readonly_fields = ("secure_url", "web_url", "thumb_url", "public_id", "width", "height", "format", "bytes", "created_at")

