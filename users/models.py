from django.db import models
from location.models import Location
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ('car_owner', 'Car Owner'),
        ('customer', 'Customer'),
        
    ]
    user_phone_number = models.CharField(max_length=20, null=True,blank=True)
    user_type = models.CharField(max_length=20, choices= USER_TYPE_CHOICES)  
    user_national_id = models.IntegerField(null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, verbose_name='user_location')
    created_at = models.DateTimeField(auto_now_add=True)
    first_name  = models.CharField(max_length=50, null=True, blank=True, verbose_name='user_first_name')
    last_name  = models.CharField(max_length=50, null=True, blank=True,verbose_name='user_last_name')
    username = models.CharField( max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(null=True, blank=True,verbose_name='user_email')
    password = models.CharField(max_length= 1000, null=True, blank=True, verbose_name='user_pasword')

    def __str__(self):
        return self.username

