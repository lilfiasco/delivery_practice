from django.contrib import admin
from .models import CustomUser, Coworker
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Регистрация модели CustomUser в админ панели"""

    list_display = ('phone_number',)
    list_filter = ('phone_number', 'first_name', 'last_name',)
    search_fields = ('phone_number', 'first_name', 'last_name',)
    filter_horizontal = ()
    ordering = ('phone_number',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)}),
    )

    add_fieldsets = (
        ("User Details", {'fields': ('phone_number', 'password', 'password2',)}),
    )


@admin.register(Coworker)
class CoworkerAdmin(admin.ModelAdmin):
    """Регистрация модели Coworker в админ панели"""

    list_display = ('phone_number',)
    list_filter = ('phone_number', 'first_name', 'last_name', 'franchise',)
    search_fields = ('phone_number', 'first_name', 'last_name', 'franchise',)
    filter_horizontal = ()
    ordering = ('phone_number',)

    fieldsets = (
        (None, {'fields': ('phone_number', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_coworker', 'franchise', 'groups', 'user_permissions',)}),
    )

    add_fieldsets = (
        ("User Details", {'fields': ('phone_number', 'password', 'password2',)}),
    )
