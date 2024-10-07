from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User  # Import your custom user model

class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('username', 'email', 'aadhaar_number', 'voter_id', 'mobile_number', 'is_verified', 'is_staff', 'is_active', 'date_joined')  # Fields to display
    list_filter = ('is_staff', 'is_active', 'is_verified')  # Filters available in the admin panel
    search_fields = ('username', 'email', 'aadhaar_number', 'voter_id', 'mobile_number')  # Enable search
    ordering = ('username',)  # Default ordering by username
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('aadhaar_number', 'voter_id', 'mobile_number', 'is_verified')}),
    )  # Adding custom fields to the user admin

# Register your custom user model with the admin site
admin.site.register(User, UserAdmin)
