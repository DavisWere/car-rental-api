from django.urls import path
from rest_framework.routers import DefaultRouter
from car.views import CarViewSet, PDFView

car_router = DefaultRouter()
car_router.register(r"cars",CarViewSet)

urlpatterns = [
    path('cars/download/report/', PDFView.as_view(), name='car-list-pdf'),
]
urlpatterns += car_router.urls