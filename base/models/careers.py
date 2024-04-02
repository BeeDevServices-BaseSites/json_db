from django.db import models
from rest_framework import serializers


class Career(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)
    position = models.TextField(max_length=200)
    type = models.TextField(max_length=50)
    location = models.TextField(max_length=50)
    salary = models.IntegerField()
    about = models.TextField()
    requirements = serializers.ListField()
    responsibilities = serializers.ListField()
    able_to_do = serializers.ListField()

