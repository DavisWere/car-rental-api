from rest_framework import viewsets, permissions
from car.models import Car
from car.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_permissions(self):
        # Allow viewing (retrieving) cars for anyone, including unauthenticated users
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        
        # Require authentication for other actions like creating, updating, and deleting cars
        return [permissions.IsAuthenticated()]
