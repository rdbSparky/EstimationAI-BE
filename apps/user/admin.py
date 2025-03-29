from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("full_name", "email", "role", "department", "is_admin", "is_staff", "created_at", "updated_at")
    search_fields = ("full_name", "email", "role__name", "department__name")
    list_filter = ("role", "department", "is_admin", "is_staff", "created_at")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("full_name", "role", "department")}),
        ("Permissions", {"fields": ("is_admin", "is_staff")}),
        ("Important Dates", {"fields": ("created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("full_name", "email", "password", "role", "department", "is_admin", "is_staff"),
        }),
    )
    filter_horizontal = ()