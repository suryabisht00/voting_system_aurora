from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VoterID  # Import your model

class VoterIDAdmin(admin.ModelAdmin):
    list_display = ('user', 'voter_id', 'name', 'father_name', 'dob', 'gender', 'created_at')  # Fields to display in the list view
    search_fields = ('user__username', 'voter_id', 'name', 'father_name')  # Enable search on these fields
    ordering = ('created_at',)  # Default ordering by created_at
    list_filter = ('gender',)  # Enable filtering by gender

# Register your model with the admin site
admin.site.register(VoterID, VoterIDAdmin)
