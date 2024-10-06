from django.db import models
from payment.models import Payment

class Billing(models.Model):
    class BillingStatus(models.TextChoices):
        PAID = 'paid', 'Paid'
        PENDING = 'pending', 'Pending'
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(unique=True)
    amount_due = models.FloatField()
    amount_paid = models.FloatField(default=0)
    billing_status = models.CharField(max_length=10, choices=BillingStatus.choices, default=BillingStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.invoice_number}"

