from django.db import models
from common.models import BaseModel

# Create your models here.

class Company(BaseModel):
    owner_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name