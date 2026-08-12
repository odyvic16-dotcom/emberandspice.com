from django.db import models

class MenuItem(models.Model):

    CATEGORY_CHOICES = [
        ("Starters", "Starters"),
        ("Main Course", "Main Course"),
        ("Desserts", "Desserts"),
        ("Drinks", "Drinks"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="menu")
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name