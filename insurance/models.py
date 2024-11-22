from django.db import models
from car.models import Car

class CarInsurance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    policy_number = models.CharField(max_length=100, unique=True,verbose_name='car_insurance_policy_number')
    provider = models.CharField(max_length=100, verbose_name='car_insurance_provider')
    start_date = models.DateTimeField(verbose_name='car_insurance_start_date')
    expiry_date = models.DateTimeField(verbose_name='car_insurance_expiry_date')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='car_insurance_created_at')

    def __str__(self):
        return f"Insurance {self.policy_number} for {self.car.car_number_plate}"

