"""
Defines the database models for the task manager application.
It includes the Task model, which represents a task with fields
for title, description, category, deadline, and priority
"""
# tasks/models.py

from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_deadline_date(date) -> None:
    """Checks if the date entered is in the past. If so,
    raise a ValidationError"""

    if date < timezone.now().date():
        raise ValidationError("Oops🤔. The deadline date cannot be "
                              "in the past."
                              )


PRIORITY_CHOICES = [  # Choices for the priority level field
    (1, 'High'),
    (2, 'Medium'),
    (3, 'Low'),
]


# Create your models here.
class Task(models.Model):
    """A subclass representing a task"""

    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=30)
    # Represented in Python by a datetime.date instance
    deadline = models.DateField(validators=[validate_deadline_date])
    priority = models.IntegerField(
        choices=PRIORITY_CHOICES,
        default=PRIORITY_CHOICES[2],
        )

    # def get_absolute_url(self):
    #     """Docstring"""
    #     return reverse('view_task', args=[str(self.id)])

    def __str__(self) -> str:
        """Returns the task title as a string"""

        return f'{self.title}'
