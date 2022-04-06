from django.db import models
from django.contrib.auth.models import AbstractUser


class myUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name = 'возраст')
    email = models.EmailField(max_length=100, unique=True)
