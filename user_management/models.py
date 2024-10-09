
from django.db import models

# 1. Admin Table Model
class Admin(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.user_id

# 2. Candidate Table Model
class Candidate(models.Model):
    candidate_name = models.CharField(max_length=255)
    constituency = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.candidate_name} - {self.constituency}"

# 3. Citizen's Data Table Model
class CitizenData(models.Model):
    citizen_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = models.DateField()
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    aadhaar_number = models.CharField(max_length=12, unique=True)
    voter_id_number = models.CharField(max_length=10, unique=True)
    photo_aadhaar = models.ImageField(upload_to='photos/aadhaar/')
    photo_voter = models.ImageField(upload_to='photos/voter/')

    def __str__(self):
        return self.citizen_name
