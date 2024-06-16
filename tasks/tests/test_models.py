"""
Unit tests for the Task model in the tasks application

This module contains a test case class 'TestViews' which inherits from
Django's 'TestCase'. The class contains various tests that verify the
expected behaviour and constraints of the model fields
"""
# tasks/tests

import datetime
from django.test import TestCase
from tasks.models import Task


# Create your tests here.
class TestModel(TestCase):
    """
    A subclass that inherits from TestCase

    It contains five tests for verifying the behaviour and constraints
    of the Task model
    """

    # Use 'setUpTestData' because data will not be modified in any tests
    @classmethod
    def setUpTestData(cls) -> None:
        """Set up test data for the Task model

        This method is called once for the TestCase class to set up non-
        modifiable test data
        """
        Task.objects.create(
            title="My task",
            description="My new task",
            category="General",
            deadline=datetime.date.today(),
            priority=1
            )

    def test_str_method_in_task_model(self) -> None:
        """
        Test the __str__ method of the Task model

        Ensure that the string representation of a object is equal to
        its title
        """
        task = Task.objects.get(id=1)
        self.assertEqual(str(task), task.title)

    def test_title_field_label_in_task_model(self):
        """
        Test the verbose name of the title field in the Task model

        Ensure that the verbose name of the title field is 'title'
        """
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_field_label_in_task_model(self):
        """
        Test the verbose name of the description field in the Task model

        Ensure that the verbose name of the description field is
        'description'
        """
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_title_field_max_length_in_task_model(self):
        """
        Test the maximum length of the title field in the Task model

        Ensure that the maximum length of the title field is 50
        characters
        """
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_category_field_max_length_in_task_model(self):
        """
        Test the maximum length of the category field in the Task model

        Ensure that the maximum length of the category field is 30
        characters
        """
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('category').max_length
        self.assertEqual(max_length, 30)
