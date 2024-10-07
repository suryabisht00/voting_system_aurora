# for addding detail menulally in admin panel for varifaication of user at the time of voting

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    voter_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)
    constituency = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
