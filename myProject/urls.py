from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/landscaping/', views.service_detail, name='service_detail'),
    path('projects/', views.projects, name='projects'),
    path('projects/burrawang-estate/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
]

