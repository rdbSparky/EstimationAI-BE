from django.db import models
from common.models import BaseModel
from apps.user.models import User
from common.models import UploadedFile

# Create your models here.

class Ingestion(BaseModel):
    name = models.CharField(max_length=255)
    file_url = models.ForeignKey(UploadedFile, on_delete=models.SET_NULL, blank=True, null=True)  # Assuming it's a file key for S3
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name