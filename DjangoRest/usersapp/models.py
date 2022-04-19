from django.db import models
from django.contrib.auth.models import AbstractUser


class myUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name = 'возраст', default=33)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
