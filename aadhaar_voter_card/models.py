from django.db import models

# Create your models here.
from django.db import models

# 1. Aadhaar Verification Model
class AadhaarVerification(models.Model):
    citizen = models.ForeignKey('user_management.CitizenData', on_delete=models.CASCADE)
    upload_aadhaar_data_status = models.BooleanField(default=False)  # Match or not
    upload_voter_card_data_status = models.BooleanField(default=False)  # Match or not
    upload_photo_status = models.BooleanField(default=False)  # Match or not

    def __str__(self):
        return f"Verification for {self.citizen.citizen_name}"
