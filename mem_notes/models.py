from django.contrib.auth.models import User
from django.db import models
from location_field.models.plain import PlainLocationField


class Memories(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city', 'location'], zoom=3)
