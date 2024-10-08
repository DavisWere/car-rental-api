from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from rental.models import Rental
from users.models import User
from car.models import Car

class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        MPESA = 'mpesa', 'Mpesa'
        CREDIT_CARD = 'credit_card', 'Credit Card'
        CASH = 'cash', 'Cash'
    
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.customer and self.rental.customer != self.customer:
            raise ValidationError("Payment customer does not match the rental customer.")

        if self.amount_paid == 0:
            self.rental.rental_status = Rental.RentalStatus.CANCELLED
            self.rental.car.status = Car.CarStatus.AVAILABLE
        elif 0 < self.amount_paid < self.rental.total_cost:
            self.rental.rental_status = Rental.RentalStatus.ONGOING
            self.rental.car.status = Car.CarStatus.RENTED
        elif self.amount_paid >= self.rental.total_cost:
            self.rental.rental_status = Rental.RentalStatus.COMPLETED
            if self.rental.return_date and self.rental.return_date <= timezone.now():
                self.rental.car.status = Car.CarStatus.AVAILABLE
            else:
                self.rental.car.status = Car.CarStatus.RENTED

        self.rental.car.save()
        self.rental.save()

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"Payment {self.id} for Rental {self.rental.id}"