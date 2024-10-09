from django.contrib import admin
from .models import Admin, Candidate, CitizenData

# Register Admin model
@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'mobile', 'email')
    search_fields = ('user_id', 'email', 'mobile')

# Register Candidate model
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('candidate_name', 'constituency', 'party', 'vote_count', 'photo')  # Added photo
    search_fields = ('candidate_name', 'constituency', 'party')
    list_filter = ('constituency', 'party')


# Register CitizenData model
@admin.register(CitizenData)
class CitizenDataAdmin(admin.ModelAdmin):
    list_display = ('citizen_name', 'father_name', 'gender', 'dob', 'mobile', 'email', 'aadhaar_number', 'voter_id_number', 'constituency')  # Added 'constituency'
    search_fields = ('citizen_name', 'aadhaar_number', 'voter_id_number', 'mobile', 'email')
    list_filter = ('gender', 'dob', 'constituency')  # Added 'constituency' to list_filter
