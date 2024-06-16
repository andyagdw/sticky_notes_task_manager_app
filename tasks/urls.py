"""
Defines the URL patterns for the task manager application.
It maps URL paths to the corresponding view functions,
enabling navigation and interaction within the application.
"""
# tasks/urls.py
from django.urls import path
from . import views

# Namespacing URL names
app_name = "tasks"  # Set the application namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('task/view/<int:task_id>/', views.view_task, name='view_task'),
    path('task/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('task/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
