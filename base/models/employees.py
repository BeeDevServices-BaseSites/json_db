from django.db import models
from rest_framework import serializers

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    photo = models.TextField(max_length=200)
    position = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    about = models.TextField()
    technologies = serializers.ListField()
    is_mentor = models.BooleanField(default=False)
    is_tutor = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_TA = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
