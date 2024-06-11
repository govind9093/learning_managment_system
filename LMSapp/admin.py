from django.contrib import admin
from .models import Course,Progress,UserProfile,Lesson


admin.site.register(UserProfile)
admin.site.register(Course)
admin.site.register(Progress)
admin.site.register(Lesson)
