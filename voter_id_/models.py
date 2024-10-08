from django.db import models
from user_management.models import User

class VoterID(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to user
    voter_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()  # Date of birth
    address = models.TextField()
    gender = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='voter_photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    constituency = models.CharField(max_length=100, null=True, blank=True)  # New field
