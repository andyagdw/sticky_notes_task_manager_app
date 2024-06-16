"""
Configures the Django admin interface for the task manager
application
"""
# tasks/admin.py

from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
