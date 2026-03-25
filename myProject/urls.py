from django.contrib import admin
from django.urls import path

from myApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("insights/", views.insights, name="insights"),
    path("insights/<slug:slug>/", views.insight_detail, name="insight_detail"),
    path("services/", views.services, name="services"),
    path("services/<slug:slug>/", views.service_detail, name="service_detail"),
    path("projects/", views.projects, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("contact/", views.contact, name="contact"),
    # Dashboard / auth
    path("dashboard/login/", views.DashboardLoginView.as_view(), name="dashboard_login"),
    path("dashboard/logout/", views.dashboard_logout, name="dashboard_logout"),
    path("dashboard/", views.dashboard_home, name="dashboard_home"),
    path("dashboard/services/", views.dashboard_services, name="dashboard_services"),
    path("dashboard/services/<int:pk>/", views.dashboard_service_edit, name="dashboard_service_edit"),
    path("dashboard/projects/", views.dashboard_projects, name="dashboard_projects"),
    path("dashboard/projects/<int:pk>/", views.dashboard_project_edit, name="dashboard_project_edit"),
    path("dashboard/projects/<int:pk>/gallery/", views.dashboard_project_gallery, name="dashboard_project_gallery"),
    path("dashboard/gallery/", views.dashboard_gallery, name="dashboard_gallery"),
    # Gallery API (JSON)
    path("dashboard/api/gallery/images/", views.gallery_api_images, name="gallery_api_images"),
    path("dashboard/api/gallery/upload/", views.gallery_api_upload, name="gallery_api_upload"),
    path("dashboard/api/editor/image-upload/", views.editor_image_upload, name="editor_image_upload"),
    # Insights dashboard
    path("dashboard/insights/", views.dashboard_insights, name="dashboard_insights"),
    path("dashboard/insights/create/", views.dashboard_insight_create, name="dashboard_insight_create"),
    path("dashboard/insights/<int:pk>/", views.dashboard_insight_edit, name="dashboard_insight_edit"),
    path("dashboard/insights/<int:pk>/delete/", views.dashboard_insight_delete, name="dashboard_insight_delete"),
    path("dashboard/insights/<int:pk>/toggle/", views.dashboard_insight_toggle, name="dashboard_insight_toggle"),
]

