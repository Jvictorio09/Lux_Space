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