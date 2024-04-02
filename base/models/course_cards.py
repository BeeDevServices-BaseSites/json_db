from django.db import models
from rest_framework import serializers


class CourseCard(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_full_course = models.BooleanField(default=True)
    is_mini_course = models.BooleanField(default=True)
    is_popular = models.BooleanField(default=True)
    is_tutoring = models.BooleanField(default=True)
    title = models.TextField(max_length=50)
    summary = serializers.ListField()
    price = models.IntegerField()
    units = models.IntegerField()
    is_on_sale = models.BooleanField(default=True)
    receipt_description = models.TextField(max_length=50)
    percent = models.IntegerField()
    has_checkout = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    image = models.TextField()

    