from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """CUSTOM USER MODEL"""

    avatar = models.ImageField(null=True))
    gender = models.CharField(max_length=10, null=True)
    bio = models.TextField(default="")
    