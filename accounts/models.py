from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# there is also ,AbstractBaseUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=10)
    is_phone_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]
    objects=UseManager()
