from django.contrib import admin
from django.urls import path

from myApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
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
]

