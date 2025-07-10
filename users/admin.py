# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add any fields you want to see in the admin list view
    list_display = ['username', 'email', 'is_staff', 'is_active']
    # Add custom fields to the admin form if you add any to the model later
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('your_custom_field',)}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('your_custom_field',)}),
    # )

admin.site.register(CustomUser, CustomUserAdmin)