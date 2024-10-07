from django.db import models

# Create your models here.
from django.db import models
from user_management.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    constituency = models.CharField(max_length=100)

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    blockchain_hash = models.CharField(max_length=64, unique=True)  # Blockchain record
    timestamp = models.DateTimeField(auto_now_add=True)

