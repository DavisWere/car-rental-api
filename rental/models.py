from django.db import models
from car.models import Car
from users.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

class Rental(models.Model):
    class RentalStatus(models.TextChoices):
        ONGOING = 'ongoing', 'Ongoing'
        COMPLETED = 'completed', 'Completed'
        CANCELLED = 'cancelled', 'Cancelled'
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='rental_customer')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='rental_car')
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField()
    rental_status = models.CharField(max_length=10, choices=RentalStatus.choices, default=RentalStatus.ONGOING)
    total_cost = models.FloatField(editable=False,verbose_name='rental_total_cost')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='rental_created_at')
    
    def save(self, *args, **kwargs):
        # Check if this is a new record (pk is None) to avoid triggering past-date validation on updates
        if self.pk is None:
            if self.rental_date and self.rental_date < timezone.now():
                raise ValidationError("Rental date cannot be in the past.")

        # Calculate the total cost based on return date and car's daily rental rate
        if self.return_date:
            rental_duration = (self.return_date - self.rental_date).days
            if rental_duration <= 0:
                rental_duration = 1
            self.total_cost = rental_duration * self.car.daily_rental_rate
        else:
            self.total_cost = 0.0

        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Rental {self.id} by {self.customer.username}"
    


