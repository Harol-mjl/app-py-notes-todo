from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    type =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)