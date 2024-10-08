from rest_framework import viewsets, permissions
from users.models import User
from car.models import Car
from rental.models import Rental
from payment.models import Payment
from payment.serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

