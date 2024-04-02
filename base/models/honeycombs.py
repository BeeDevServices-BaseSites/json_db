from django.db import models
from rest_framework import serializers

class Honeycombs(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    link = models.TextField()
    tag = models.TextField(max_length=50)
