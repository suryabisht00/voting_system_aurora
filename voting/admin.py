from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Candidate, Vote  # Import your models

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'constituency')  # Fields to display in the list view
    search_fields = ('name', 'party', 'constituency')  # Enable search on these fields
    ordering = ('name',)  # Default ordering by name

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'candidate', 'blockchain_hash', 'timestamp')  # Fields to display
    search_fields = ('user__username', 'candidate__name', 'blockchain_hash')  # Search fields
    ordering = ('timestamp',)  # Default ordering by timestamp
    list_filter = ('candidate',)  # Enable filtering by candidate

# Register your models with the admin site
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote, VoteAdmin)
