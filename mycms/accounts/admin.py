from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from . import forms

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    add_form = forms.RegisterForm
    form = forms.CustomUserChangeForm

    ordering = ('email',)
    list_display = [
        "email",
        "name",
        "is_active",
        "is_staff",
    ]

    search_fields = ['email']
    fieldsets = (
        (None, {
            "fields": (
                'email', 'password',
            ),
        }),
        ('Details', {
            "fields": (
                'name', 'slug',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_active', 'is_staff', 
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            "classes": ('wide',),
            "fields": ('email', 'name', 'mobile', 'password1', 'password2'),
        }),
    ),