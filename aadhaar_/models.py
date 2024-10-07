from django.db import models

# Create your models here.
from django.db import models
from user_management.models import User

class Aadhaar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to user
    aadhaar_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of birth
    address = models.TextField()
    gender = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='aadhaar_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
