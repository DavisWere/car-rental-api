from django.db import models

class Location(models.Model):
    country_of_residence = models.CharField(max_length=100,verbose_name='location_country_of_residence')
    city = models.CharField(max_length=100,verbose_name='location_city')
    constituency = models.CharField(max_length=100,verbose_name='location_constituency')
    street = models.CharField(max_length=255, verbose_name='location_street')
    address = models.CharField(max_length=255, verbose_name='location_address')
    apartment_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='location_apartment_number')

    def __str__(self):
        return f"{self.city}, {self.country_of_residence}"

