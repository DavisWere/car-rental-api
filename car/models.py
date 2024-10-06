from django.db import models
from users.models import User

class Car(models.Model):
    class CarStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available'
        RENTED = 'rented', 'Rented'
        
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_manufactured_year = models.DateField()
    car_number_plate = models.CharField(max_length=20, unique=True)
    car_chesis_number = models.CharField(max_length=50, unique=True)
    car_logbook = models.FileField(upload_to='logbooks/')
    daily_rental_rate = models.FloatField()
    status = models.CharField(max_length=10, choices=CarStatus.choices, default=CarStatus.AVAILABLE)

    def __str__(self):
        return self.car_number_plate

