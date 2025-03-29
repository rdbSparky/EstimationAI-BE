from django.contrib import admin
from .models import Ingestion

@admin.register(Ingestion)
class IngestionAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "file_url", "created_at", "updated_at")
    search_fields = ("name", "user__email")  # Assuming User has an email field
    list_filter = ("created_at", "updated_at", "user")
    ordering = ("-created_at",)
