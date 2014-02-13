from django.db import models

class Tasks(models.Model):
    owner = models.ForeignKey('auth.User', related_name='tasks')
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
