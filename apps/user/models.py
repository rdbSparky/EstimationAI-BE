from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from common.models import BaseModel
from apps.department.models import Department
from apps.role.models import Role

# Create your models here.

class MyUserManager(BaseUserManager):
    """The Custom BaseManager Class"""

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email
        """
        user = self.create_user(email, password=password)
        user.is_super_user = True
        user.is_company_owner = True
        user.is_staff = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser, BaseModel):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    def __str__(self):
        return self.full_name

