# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    voter_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    mobile_number = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)

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
