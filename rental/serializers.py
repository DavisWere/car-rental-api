from rest_framework import serializers
from django.utils import timezone
from rental.models import Rental
from car.models import Car
from users.models import User

class RentalSerializer(serializers.ModelSerializer):
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(), write_only=True, required=False
    )
    customer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, required=False
    )
    
    customer_details = serializers.SerializerMethodField(read_only=True)
    car_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rental
        fields = [
            'id', 'customer', 'car', 'customer_details', 'car_details',
            'rental_date', 'return_date', 'rental_status', 'total_cost', 'created_at'
        ]
        
    def get_customer_details(self, obj):
        if obj.customer:
            return {
                "first name": obj.customer.first_name,
                "last name": obj.customer.last_name,
                "email": obj.customer.email
            }
        return None
    
    def get_car_details(self, obj):
        if obj.car:
            return {
                "number plate": obj.car.car_number_plate,
                "model": obj.car.car_model,
                "daily rental rate": obj.car.daily_rental_rate
            }
        return None

    def validate(self, attrs):
        rental_date = attrs.get('rental_date')
        return_date = attrs.get('return_date')
        car = attrs.get('car')

        if car is None:
            raise serializers.ValidationError("Car must be provided.")

    
        if not self.instance:  
            if rental_date and rental_date < timezone.now():
                raise serializers.ValidationError("Rental date cannot be in the past.")

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