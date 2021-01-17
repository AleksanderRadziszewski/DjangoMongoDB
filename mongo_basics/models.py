from django.db import models


class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
    roll_number = models.CharField(max_length=20)
