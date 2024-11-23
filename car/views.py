from rest_framework import viewsets, permissions
from car.models import Car
from car.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    """
    ViewSet to manage Car objects with filtering based on car_owner.
    """
    serializer_class = CarSerializer
    queryset= Car.objects.all()

    def get_queryset(self):
        """
        Filters cars based on the logged-in user.
        """
        user = self.request.user
        if self.action in ['list', 'retrieve']:  
            return Car.objects.all()
        if user.is_authenticated:
            return Car.objects.filter(car_owner=user)
        return Car.objects.none()  

    def get_permissions(self):
        """
        Assign permissions based on the action.
        """
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]  
        return [permissions.IsAuthenticated()]  


