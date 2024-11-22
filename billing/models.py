from django.db import models
from payment.models import Payment

class Billing(models.Model):
    class BillingStatus(models.TextChoices):
        PAID = 'paid', 'Paid'
        PENDING = 'pending', 'Pending'
    
    payment = models.ForeignKey(
        Payment, 
        on_delete=models.CASCADE, 
        verbose_name='billing_payment'
    )
    invoice_number = models.IntegerField(
        unique=True, 
        verbose_name='billing_invoice_number'
    )
    amount_due = models.FloatField(
        verbose_name='billing_amount_due'
    )
    amount_paid = models.FloatField(
        default=0, 
        verbose_name='billing_amount_paid'
    )
    billing_status = models.CharField(
        max_length=10, 
        choices=BillingStatus.choices, 
        default=BillingStatus.PENDING, 
        verbose_name='billing_status'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='billing_created_at'
    )


    def __str__(self):
        return f"Invoice {self.invoice_number}"

