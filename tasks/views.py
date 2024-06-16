"""
Defines the view functions for the task manager application.
It handles HTTP requests and returns appropriate HTTP responses,
rendering templates and performing CRUD operations on the Task model.
"""
# tasks/views.py
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.utils import timezone
import pytz
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """
    Retrieves the id, title, and description of:

    1. All tasks
    2. All tasks that are due today
    3. All tasks that have passed their deadline date

    from the database and renders the index template

    Parameters
    ----------
    request: HttpRequest
        Contains metadata about the request

    Returns
    ----------
    HttpResponse | HttpResponseRedirect
    """

    # Get results as namedtuple()
    tasks = (Task.objects.
             order_by("title").
             values_list("id", "title", "description", named=True
                         )
             )

    now_utc = timezone.now()  # Get current time in UTC
    london_timezone = pytz.timezone('Europe/London')
    # Convert current time to London time zone as UTC is 1 hour behind
    now_london = now_utc.astimezone(london_timezone).date()

    tasks_due_today = (  # Get tasks
        Task.objects.
        order_by("title").
        filter(deadline=now_london).
        values_list("id", "title", "description", named=True
                    )
        )

    tasks_passed_deadline = (
        Task.objects.
        order_by("deadline").
        filter(deadline__lt=now_london).
        values_list("id", "title", "description", named=True
                    )
        )

    # Check if form has been submitted and save task (if valid)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Task was created successfully')
            form.save()
            return redirect('tasks:index')
    else:
        form = TaskForm()  # Display task form

    context = {
        'tasks': tasks,
        'tasks_due_today': tasks_due_today,
        'tasks_passed_deadline': tasks_passed_deadline,
        'form': form,
    }

    return render(request, 'index.html', context=context)


def view_task(request: HttpRequest, task_id: int) -> HttpResponse:
    """
    It retrieves the id, title, and description of:

    1. Tasks with the same deadline as the task_id
    2. Tasks with the same category as the task_id
    3. Tasks with the same priority as the task_id

    from the database and then renders the view_task template

    Parameters
    ----------
    request: HttpRequest
        Contains metadata about the request
    task_id: int
        Represents the id of the task

    Returns
    ----------
    HttpResponse | HttpResponseRedirect
    """

    # If task does not exist, raise an error
    task = get_object_or_404(Task, id=task_id)

    # Get tasks that are related to the current task
    # Randomise the order of the QuerySet
    tasks_with_same_deadline = (
        Task.objects.
        filter(deadline=task.deadline).
        exclude(id=task.id).
        order_by("?").
        values_list("id", "title", "description", named=True
                    )[:4]
        )

    tasks_with_same_category = (
        Task.objects.
        filter(category=task.category).
        exclude(id=task.id).
        order_by("?").
        values_list("id", "title", "description", named=True
                    )[:4]
        )

    tasks_with_same_priority = (
        Task.objects.
        filter(priority=task.priority).
        exclude(id=task.id).
        order_by("?").
        values_list("id", "title", "description", named=True
                    )[:4]
        )

    context = {
        'task': task,
        'tasks_with_same_deadline': tasks_with_same_deadline,
        'tasks_with_same_category': tasks_with_same_category,
        'tasks_with_same_priority': tasks_with_same_priority,
    }

    return render(request, 'view_task.html', context=context)


def edit_task(request: HttpRequest,
              task_id: int) -> HttpResponse | HttpResponseRedirect:
    """
    It retrieves a task from the database and renders the edit_task
    page

    Parameters
    ----------
    request: HttpRequest
        Contains metadata about the request
    task_id: int
        Represents the id of the task

    Returns
    ----------
    HttpResponse | HttpResponseRedirect
    """

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        # Create a TaskForm instance with submitted data, and bind it
        # to the existing task instance
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if form.has_changed():
                messages.success(request, 'Task was updated successfully')
                form.save()
            return redirect('tasks:view_task', task_id=task.id)
    else:
        # Creates a TaskForm instance pre-filled with the current task
        # data if form is being accessed for the first time
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }

    return render(request, 'edit_task.html', context=context)


@require_POST  # Deletion should be done via a POST request
def delete_task(request: HttpRequest,
                task_id: int) -> HttpResponseRedirect:
    """
    Retrieves a task from the database and deletes it.

    Parameters
    ----------
    request: HttpRequest
        Contains metadata about the request
    task_id: int
        Represents the id of the task

    Returns
    ----------
    HttpResponse | HttpResponseRedirect
    """

    task = get_object_or_404(Task, id=task_id)
    task.delete()
    messages.success(request, 'Task was deleted successfully')
    return redirect('tasks:index')
