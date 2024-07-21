from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=20, unique=True)
    content = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
