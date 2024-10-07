from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'aadhaar_number', 'voter_id', 'mobile_number', 'is_verified', 'constituency', 'address', 'father_name', 'dob')
    fields = ('username', 'aadhaar_number', 'voter_id', 'mobile_number', 'is_verified', 'constituency', 'address', 'father_name', 'dob', 'password', 'groups', 'user_permissions')

    def save_model(self, request, obj, form, change):
        if not change and User.objects.filter(mobile_number=obj.mobile_number).exists():
            raise ValidationError('Mobile number must be unique.')
        super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
