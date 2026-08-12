from django.shortcuts import render
from .models import MenuItem

def menu(request):

    items = MenuItem.objects.filter(available=True)

    categories = [
        "Starters",
        "Main Course",
        "Desserts",
        "Drinks",
    ]

    context = {
        "items": items,
        "categories": categories,
    }

    return render(request, "menu/menu.html", context)