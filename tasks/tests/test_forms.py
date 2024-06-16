"""
Unit tests for the TaskForm class in the tasks app

This module contains a test case class 'TestForm' which inherits from
Django's 'SimpleTestCase'. The class contains various tests that
validate the behaviour of the TaskForm class
"""
# tasks/tests

import datetime
from django.test import SimpleTestCase
from tasks.forms import TaskForm


# Use 'SimpleTestCase' - no interaction with a db or test client
class TestForm(SimpleTestCase):
    """
    A subclass that inherits from SimpleTestCase

    It contains seven tests to validate the behaviour of the TaskForm
    class
    """

    def setUp(self):
        """Creates a new form instance for each test"""
        self.form = TaskForm()
        # Todays date in YYYY-MM-DD format
        self.current_day = datetime.date.today()
        self.task_title = "My task"
        self.task_description = "My new task"
        self.task_category = 'General'
        self.task_priority = '1'

    def test_task_form_title_field_label(self):
        """
        Test whether the label of the 'title' field in TaskForm is
        either None or "Title"
        """
        # Check none as value is not explicity set on this field
        # Django capitalises label if not set explicitly
        self.assertTrue(self.form.fields['title'].label is None or
                        self.form.fields['title'].label
                        == 'Title')

    def test_task_form_description_field_label(self):
        """
        Test whether the label of the 'description' field in TaskForm
        is either None or "Description"
        """
        self.assertTrue(self.form.fields['description'].label is None or
                        self.form.fields['description'].label
                        == 'Description')

    def test_task_form_category_field_label(self):
        """
        Test whether the label of the 'category' field in TaskForm is
        either None or "Category"
        """
        self.assertTrue(self.form.fields['category'].label is None or
                        self.form.fields['category'].label
                        == 'Category')

    def test_task_form_deadline_field_label(self):
        """
        Test whether the label of the 'deadline' field in TaskForm is
        either None or 'Deadline'.
        """
        self.assertTrue(self.form.fields['deadline'].label is None or
                        self.form.fields['deadline'].label
                        == 'Deadline')

    def test_task_form_priority_field_label(self):
        """
        Test whether the label of the 'priority' field in TaskForm is
        either None or 'Priority'.
        """
        self.assertTrue(self.form.fields['priority'].label is None or
                        self.form.fields['priority'].label
                        == 'Priority')

    def test_task_form_valid_data(self):
        """Test whether the form is valid with valid data"""
        form = TaskForm(data={
            'title': self.task_title,
            'description': self.task_description,
            'category': self.task_category,
            'deadline': str(self.current_day),  # Change to string
            'priority': self.task_priority
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(len(form.errors), 0)

    def test_task_form_not_valid_deadline_in_past(self):
        """
        Test whether the form is not valid when the deadline is in the
        past
        """
        form = TaskForm(data={
            'title': self.task_title,
            'description': self.task_description,
            'category': self.task_category,
            # Yesterday date
            'deadline': str(self.current_day - datetime.timedelta(days=1)),
            'priority': self.task_priority
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # Deadline error
