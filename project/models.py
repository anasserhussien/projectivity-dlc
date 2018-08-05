from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.TextField(unique = True)
    desc = models.TextField()
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    assignee = models.ManyToManyField(User, related_name = 'assignee')

    def __str__(self):
        return self.title
