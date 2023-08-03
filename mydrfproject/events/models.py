# events/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add custom fields if necessary

    def __str__(self):
        return self.username

class Event(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    total_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
