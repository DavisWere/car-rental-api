from rest_framework import serializers
from django.utils import timezone
from payment.models import Payment
from rental.models import Rental
from car.models import Car

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'customer', 'rental', 'amount_paid', 
                'payment_date', 'payment_method', 'created_at']
    
    def validate(self, attrs):
        customer = attrs.get('customer')
        rental = attrs.get('rental')
        amount_paid = attrs.get('amount_paid')

        if customer and rental.customer != customer:
            raise serializers.ValidationError("Payment customer does not match the rental customer.")

        if amount_paid == 0:
            rental.rental_status = Rental.RentalStatus.CANCELLED
            rental.car.status = Car.CarStatus.AVAILABLE
        elif 0 < amount_paid < rental.total_cost:
            rental.rental_status = Rental.RentalStatus.ONGOING
            rental.car.status = Car.CarStatus.RENTED
        elif amount_paid >= rental.total_cost:
            rental.rental_status = Rental.RentalStatus.COMPLETED
            if rental.return_date and rental.return_date <= timezone.now():
                rental.car.status = Car.CarStatus.AVAILABLE
            else:
                rental.car.status = Car.CarStatus.RENTED  

        
        rental.car.save()
        rental.save()

        return attrs
