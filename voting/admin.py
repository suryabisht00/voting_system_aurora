from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import VotingStatus

# Register VotingStatus model
@admin.register(VotingStatus)
class VotingStatusAdmin(admin.ModelAdmin):
    list_display = ('citizen', 'constituency', 'blockchain_hash', 'status')
    search_fields = ('citizen__citizen_name', 'blockchain_hash')
    list_filter = ('status', 'constituency')
