from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import SocNetUserManager

# Create your models here.

class SocNetUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=100, unique=True)
    confirmation_code = models.CharField(max_length = 6, null = True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = SocNetUserManager()

    def __str__(self):
        return self.email