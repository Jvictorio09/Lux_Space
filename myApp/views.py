from django.shortcuts import render


def home(request):
    """
    Render the main LuxSpace landing page.
    """
    return render(request, "index.html")