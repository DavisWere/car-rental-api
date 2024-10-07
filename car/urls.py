from django.urls import path
from rest_framework.routers import DefaultRouter
from car.views import CarViewSet

car_router = DefaultRouter()
car_router.register(r"cars",CarViewSet)

urlpatterns = [
    
]
urlpatterns += car_router.urls