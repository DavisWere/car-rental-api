from rest_framework import serializers
from datetime import timedelta
from rental.models import Rental

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = ['id', 'customer', 'car', 'rental_date', 'return_date', 'rental_status', 'total_cost', 'created_at']

    def validate(self, attrs):
        rental_date = attrs.get('rental_date')
        return_date = attrs.get('return_date')
        car = attrs.get('car')

        if rental_date and return_date:
            if return_date < rental_date:
                raise serializers.ValidationError("Return date cannot be before rental date.")
            rental_duration = (return_date - rental_date).days
            
            if rental_duration <= 0:
                rental_duration = 1

            attrs['total_cost'] = rental_duration * car.daily_rental_rate
        else:
            
            attrs['total_cost'] = 0.0

        return attrs