from email.policy import default
from tkinter import CASCADE
from django.db import models

from usersapp.models import myUser

class Project(models.Model):
    name = models.CharField(max_length=64)
    repo = models.CharField(max_length=128)
    users = models.ManyToManyField(myUser)

    def __str__(self):
        return self.name


class ToDo(models.Model):

    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    date_create = models.DateTimeField()
    date_update = models.DateTimeField()
    status = models.BooleanField(default=True)
