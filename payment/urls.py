from django.urls import path
from rest_framework.routers import DefaultRouter
from payment.views import PaymentViewSet

payment_router = DefaultRouter()
payment_router.register(r'payments', PaymentViewSet)

urlpatterns = [
    
]
urlpatterns += payment_router.urls
