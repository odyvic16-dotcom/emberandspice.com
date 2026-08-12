from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    date = models.DateField()
    time = models.TimeField()

    guests = models.PositiveIntegerField()

    special_request = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Cancelled", "Cancelled"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return f"{self.name} - {self.date}"