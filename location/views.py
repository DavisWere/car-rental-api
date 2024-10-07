from django.shortcuts import render
from rest_framework import viewsets, permissions
from location.models import Location
from location.serializers import LocationSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
