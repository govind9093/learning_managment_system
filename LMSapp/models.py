from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=30)

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField(help_text="Duration in hours")
    start_date = models.DateField()
    end_date = models.DateField()
    teacher_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    language = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Lesson(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()  

class Progress(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.FloatField()
  