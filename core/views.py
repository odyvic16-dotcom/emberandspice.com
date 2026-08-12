from django.shortcuts import render

from .models import ContactMessage


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def gallery(request):
    return render(request, 'core/gallery.html')

def contact(request):
    return render(request, 'core/contact.html')

def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        return render(
            request,
            "core/contact.html",
            {"success": True}
        )

    return render(request, "core/contact.html")