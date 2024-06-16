"""
Defines the form for the task manager application.
It includes the TaskForm, which handles user input for
creating and updating tasks

Note: There is no need to define the field types as they have already
been defined in the model
"""
# tasks/forms.py

from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    A form for creating and updating Task instances

    Creates a Form class from a Django model. It will have a form field
    for every model field specified. The label used comes from the model
    """

    class Meta:
        """Defines the metadata options for the TaskForm"""
        model = Task
        # Include all the other fields apart from the id
        exclude = ['id']
        widgets = {
            # Deadline field should use a HTML5 date input
            'deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'title': forms.TextInput(
                attrs={'placeholder': "Grocery Shopping"}
            ),
            'description': forms.Textarea(
                attrs={'placeholder': "Purchase items from the grocery "
                       "list including fruits, vegetables, and "
                       "household essentials."}
            ),
            'category': forms.TextInput(
                attrs={'placeholder': 'Shopping'}
            ),
        }
        help_texts = {
            'deadline': 'Please ensure that deadline starts from today'
        }
        # Labels could be set here to

    def save(self, commit=True):
        """
        Overrides the save behaviour of the form to modify the
        category and title value before saving it to the database

        The commit parameter determines whether the changes are saved to
        the database immediately (True by default)
        """
        # Calls 'ModelForm' save method, which creates a model instance
        # but does not save it to the database yet
        instance = super(TaskForm, self).save(commit=False)

        if instance.title:  # Checks if it has a value
            instance.title = instance.title.title()

        if instance.category:
            instance.category = instance.category.title()

        # Save the instance to the database if commit is True
        if commit:
            instance.save()

        return instance
