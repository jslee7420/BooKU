from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)

class CustomUserAdmin(UserAdmin):
    UserAdmin.fieldsets[1][1]['fields']+=('university','first_major','second_major','third_major', 'date_of_birth', 'gender')
    UserAdmin.add_fieldsets +=(
        (('Additional Info'),{'fields':('university','first_major','second_major','third_major', 'date_of_birth', 'gender')}),
    )