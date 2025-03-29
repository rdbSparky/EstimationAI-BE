from django.db import models
from common.models import BaseModel
from apps.company.models import Company

# Create your models here.

class Department(BaseModel):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name