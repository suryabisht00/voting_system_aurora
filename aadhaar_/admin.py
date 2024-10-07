from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Aadhaar  # Import your Aadhaar model

class AadhaarAdmin(admin.ModelAdmin):
    list_display = ('user', 'aadhaar_number', 'name', 'father_name', 'dob', 'gender', 'mobile_number', 'created_at')  # Fields to display
    search_fields = ('user__username', 'aadhaar_number', 'name', 'father_name', 'mobile_number')  # Enable search
    ordering = ('created_at',)  # Default ordering by creation date
    list_filter = ('gender',)  # Filter by gender

# Register your model with the admin site
admin.site.register(Aadhaar, AadhaarAdmin)
