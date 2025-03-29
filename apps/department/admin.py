from django.contrib import admin
from .models import Department

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "created_at", "updated_at")
    search_fields = ("name", "company__name")
    list_filter = ("company", "created_at")
    ordering = ("name",)
