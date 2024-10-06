from django.db import models
from location.models import Location
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('car_owner', 'Car Owner'),
        ('customer', 'Customer'),
        
    ]
    user_phone_number = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20, choices= USER_TYPE_CHOICES)  
    user_national_id = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

