from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.TextField(unique = True)
    desc = models.TextField()
    admin = models.ForeignKey(User, on_delete = models.CASCADE)
    assignee = models.ManyToManyField(User, related_name = 'assignee')

    def __str__(self):
        return self.title

class Stage(models.Model):
    title = models.TextField(unique = True)
    project = models.ForeignKey(Project, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.TextField()
    content = models.TextField()
    estimated_hours = models.DecimalField()
    actual_hours = models.DecimalField()
    stage = models.ForeignKey(Stage, on_delete = models.CASCADE)
    assignee = models.ForeignKey(User, on_delete = models.CASCADE, null= True, blank = True)

    def __str__(self):
        return self.title
