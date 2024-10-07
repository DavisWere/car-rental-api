from django.urls import path
from rest_framework.routers import DefaultRouter
from location.views import LocationViewSet

location_router = DefaultRouter()

location_router.register(r"location", LocationViewSet)

urlpatterns = [
    
]
urlpatterns += location_router.urls