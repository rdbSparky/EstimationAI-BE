from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "owner_name", "email", "created_at", "updated_at")
    search_fields = ("name", "owner_name", "email")
    list_filter = ("created_at", "updated_at")
    ordering = ("name",)
