from django.db import models
from rental.models import Rental

class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        MPESA = 'mpesa', 'Mpesa'
        CREDIT_CARD = 'credit_card', 'Credit Card'
        CASH = 'cash', 'Cash'
    
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount_paid = models.FloatField()
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} for Rental {self.rental.id}"



