from django.shortcuts import render, redirect
from .models import Reservation


def reservation(request):

    if request.method == "POST":

        Reservation.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date=request.POST.get("date"),
            time=request.POST.get("time"),
            guests=request.POST.get("guests"),
            special_request=request.POST.get("special_request"),
        )

        return render(
            request,
            "reservations/reservation.html",
            {"success": True}
        )

    return render(request, "reservations/reservation.html")