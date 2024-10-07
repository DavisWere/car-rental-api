from rest_framework import viewsets, permissions
from rental.models import Rental
from rental.serializers import RentalSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    permission_classes = [permissions.IsAuthenticated]