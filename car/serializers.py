from rest_framework import serializers
from car.models import Car

class CarSerializer(serializers.ModelSerializer):
    car_owner = serializers.SerializerMethodField() 
    class Meta:
        model = Car
        fields = '__all__'
    
    def get_car_owner(self, obj):
        if obj.car_owner:
            return {
                "first name": obj.car_owner.first_name,
                "last name": obj.car_owner.last_name
            }
        return None

    def validate(self, data):
        car_owner = data.get('car_owner')

        if car_owner and car_owner.user_type != 'car_owner':
            raise serializers.ValidationError("Only users with user_type 'car_owner' can own a car.")

        return data
    
    