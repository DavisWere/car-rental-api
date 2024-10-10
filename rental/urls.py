from django.urls import path
from rest_framework.routers import DefaultRouter
from rental.views import RentalViewSet

rental_router = DefaultRouter()
rental_router.register(r"rentals", RentalViewSet)

urlpatterns = [
    
]
urlpatterns += rental_router.urls