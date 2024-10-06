from django.db import models
from car.models import Car

class CarMaintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=100)
    maintenance_date = models.DateTimeField()
    cost = models.FloatField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Maintenance for {self.car.car_number_plate}"

