from django.contrib.auth.models import AbstractUser
from django.db import models
from .model_managers import CustomUserManager



class DealerStatus(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)


class User(AbstractUser):
    username = models.CharField(max_length=254, default='user_agent')
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = None
    last_name = None
    is_admin = models.BooleanField(default=False, db_column='isadmin')
    is_staff = models.BooleanField(default=False, db_column='isstaff')
    is_superuser = models.BooleanField(default=False, db_column='issuperuser')
    is_dealer = models.BooleanField(default=False, db_column='isdealer')
    dealer_status = models.ForeignKey(DealerStatus, name="DealerStatus", on_delete=models.CASCADE, blank=True, null=True)
    USERNAME_FIELD = "email"
    EMAIL_FIELD = 'email'  # This is for logging in as superuser with the same logic as common login
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()




