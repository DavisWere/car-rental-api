from django.contrib import admin
from .models import Rental

class RentalAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'car', 'rental_date', 'return_date', 'rental_status', 'total_cost']
    readonly_fields = ['total_cost'] 

admin.site.register(Rental, RentalAdmin)