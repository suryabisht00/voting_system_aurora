from django.db import models

# Create your models here.
from django.db import models

# Assuming you have a CitizenData model in user_management app
class VotingStatus(models.Model):
    citizen = models.ForeignKey('user_management.CitizenData', on_delete=models.CASCADE)
    constituency = models.IntegerField(default=0)  # Default value for constituency
    blockchain_hash = models.CharField(max_length=255, default='0')  # Default value for blockchain hash
    status = models.CharField(max_length=10, choices=[('voted', 'Voted'), ('not_voted', 'Not Voted')], default='not_voted')

    def __str__(self):
        return f"{self.citizen.citizen_name} - {self.status}"
