from rest_framework import viewsets, permissions
from car.models import Car
from car.serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
    
        return [permissions.IsAuthenticated()]
