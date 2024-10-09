from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AadhaarVerification

# Register AadhaarVerification model
@admin.register(AadhaarVerification)
class AadhaarVerificationAdmin(admin.ModelAdmin):
    list_display = ('citizen', 'upload_aadhaar_data_status', 'upload_voter_card_data_status', 'upload_photo_status')
    list_filter = ('upload_aadhaar_data_status', 'upload_voter_card_data_status', 'upload_photo_status')
    search_fields = ('citizen__citizen_name', 'citizen__aadhaar_number', 'citizen__voter_id_number')
