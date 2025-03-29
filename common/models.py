from django.db import models
import uuid


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class UploadedFile(BaseModel):
    file_key = models.CharField(max_length=255)
    file_name=models.CharField(max_length=255)

    def __str__(self):
        return self.file.name