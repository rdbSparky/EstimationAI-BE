from rest_framework import serializers
from .models import UploadedFile
from common.cloud_services import generate_signed_url

class UploadedFileSerializer(serializers.ModelSerializer):

    signed_url=serializers.SerializerMethodField()

    class Meta:
        model = UploadedFile
        fields = ["id", "file_key", "file_name", "signed_url"]

    def get_signed_url(self, obj):
        """Generate signed URL for the stored file"""
        return generate_signed_url(obj.file_key) if obj.file_key else None
