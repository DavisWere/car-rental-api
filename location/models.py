from django.db import models

class Location(models.Model):
    country_of_residence = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    apartment_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.city}, {self.country_of_residence}"

