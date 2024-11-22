from django.db import models
from users.models import User

class Car(models.Model):
    class CarStatus(models.TextChoices):
        AVAILABLE = 'available', 'Available for rental'
        RENTED = 'rented', ' This car is rented'
        
    car_owner =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,)
    car_make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_image  = models.ImageField(upload_to='car_images/', null=True, blank=True)
    car_manufactured_year = models.DateField()
    car_number_plate = models.CharField(max_length=20, unique=True)
    car_chesis_number = models.CharField(max_length=50, unique=True)
    car_logbook = models.FileField(upload_to='logbooks/')
    car_capacity = models.PositiveSmallIntegerField(null=True, blank=True)
    car_fuel_consumption = models.CharField(max_length=10, null=True, blank=True)
    car_description = models.TextField(null=True, blank=True)
    daily_rental_rate = models.FloatField(verbose_name='car_daily_rental_rate')
    status = models.CharField(max_length=10, choices=CarStatus.choices, default=CarStatus.AVAILABLE, verbose_name='car_status')
    
    def save(self, *args, **kwargs):
        if self.car_owner and self.car_owner.user_type == 'car_owner':
            super().save(*args, **kwargs)  
        else:
            raise ValueError("you cannot own a car in this system.")

    def __str__(self):
        return self.car_number_plate

    

