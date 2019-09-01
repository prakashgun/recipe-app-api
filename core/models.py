from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField('email', unique=True)
