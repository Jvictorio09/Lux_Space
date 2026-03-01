from django.shortcuts import render


def home(request):
    """
    Render the main LuxSpace landing page.
    """
    return render(request, "index.html")


def services(request):
    """
    Render the services overview page.
    """
    return render(request, "service_overview.html")


def contact(request):
    """
    Render the contact us page.
    """
    return render(request, "contact_us.html")


def service_detail(request):
    """
    Render the service detail page (landscaping).
    """
    return render(request, "service_detail.html")


def projects(request):
    """
    Render the projects/portfolio overview page.
    """
    return render(request, "project_page/project_overview.html")


def project_detail(request):
    """
    Render the project detail page (Burrawang Estate).
    """
    return render(request, "project_page/project_details.html")