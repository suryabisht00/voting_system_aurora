from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ExtractedData, Verification  # Import your models

class ExtractedDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'extracted_name', 'extracted_father_name', 'extracted_dob', 'extracted_gender', 'created_at')  # Fields to display
    search_fields = ('user__username', 'extracted_name', 'extracted_father_name', 'extracted_aadhaar_number', 'extracted_voter_id')  # Enable search
    ordering = ('created_at',)  # Default ordering by creation date
    list_filter = ('extracted_gender',)  # Filter by gender

class VerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'aadhaar_status', 'voter_id_status', 'photo_status', 'verification_timestamp')  # Fields to display
    search_fields = ('user__username',)  # Enable search
    ordering = ('verification_timestamp',)  # Default ordering by verification timestamp

# Register your models with the admin site
admin.site.register(ExtractedData, ExtractedDataAdmin)
admin.site.register(Verification, VerificationAdmin)
