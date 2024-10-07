from django.db import models

# Create your models here.
from django.db import models
from user_management.models import User

class ExtractedData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    extracted_name = models.CharField(max_length=100)
    extracted_father_name = models.CharField(max_length=100)
    extracted_dob = models.DateField()
    extracted_address = models.TextField()
    extracted_gender = models.CharField(max_length=10)
    extracted_aadhaar_number = models.CharField(max_length=12)
    extracted_voter_id = models.CharField(max_length=10)
    extracted_photo = models.ImageField(upload_to='extracted_photos/')
    created_at = models.DateTimeField(auto_now_add=True)

class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aadhaar_status = models.BooleanField(default=False)
    voter_id_status = models.BooleanField(default=False)
    photo_status = models.BooleanField(default=False)
    verification_timestamp = models.DateTimeField(auto_now_add=True)
