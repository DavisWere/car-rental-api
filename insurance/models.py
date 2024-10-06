from django.db import models
from car.models import Car

class CarInsurance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100, unique=True)
    provider = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Insurance {self.policy_number} for {self.car.car_number_plate}"

