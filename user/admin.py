from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    UserAdmin.add_fieldsets += (
        (('Additional Info'), {
         'fields': ('first_major', 'second_major', 'third_major', 'email',  'is_active', 'is_staff',)}),
    )


admin.site.register(User, UserAdmin)
