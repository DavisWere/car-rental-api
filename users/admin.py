from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Other Fields",
            {
                "fields": (
                    'user_phone_number',
                    'user_type',
                    'user_national_id',
                    'location',
                )
            },
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Other Fields",
            {
                "fields": (
                    'email',
                    'first_name',
                    'last_name',
                    'user_phone_number',
                    'user_type',
                    'user_national_id',
                    'location',
                )
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)