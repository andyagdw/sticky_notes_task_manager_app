"""
Unit tests for URL resolution in the tasks app

This module contains a test case class 'TestUrls' which inherits from
Django's 'TestCase'. The class contains various tests that test that
the URL patterns resolve to the correct view functions in the tasks app
"""
# tasks/tests

import datetime
from django.test import TestCase
from django.urls import reverse, resolve
from tasks.views import (index,
                         view_task,
                         edit_task,
                         delete_task
                         )
from tasks.models import Task


class TestUrls(TestCase):
    """
    A subclass that inherits from TestCase

    It contains four tests that tests whether the URL patterns defined
    in the tasks app correctly resolve to their corresponding view
    functions
    """

    # Use 'setUpTestData' because data will not be modified in any tests
    @classmethod
    def setUpTestData(cls) -> None:
        """
        Set up test data for the Task model

        This method is called only once for the TestCase class to set up
        non-modifiable test data
        """
        Task.objects.create(
            title="My task",
            description="My new task",
            category="General",
            deadline=datetime.date.today(),
            priority=1
            )

    def test_index_url_resolves(self):
        """Test that the tasks:index URL resolves to the index view"""
        index_url = reverse('tasks:index')
        # resolve(url).func = tasks.views.index
        self.assertEqual(resolve(index_url).func, index)

    def test_view_task_url_resolves(self):
        """
        Test that the tasks:view_task URL resolves to the view_task
        view
        """
        task = Task.objects.get(id=1)
        view_task_url = reverse('tasks:view_task', args=[task.id])
        # resolve(url).func = tasks.views.view_task
        self.assertEqual(resolve(view_task_url).func, view_task)

    def test_edit_task_url_resolves(self):
        """
        Test that the tasks:edit_task URL resolves to the view_task view
        """
        task = Task.objects.get(id=1)
        edit_task_url = reverse('tasks:edit_task', args=[task.id])
        # resolve(url).func = tasks.views.edit_task
        self.assertEqual(resolve(edit_task_url).func, edit_task)

    def test_delete_task_url_resolves(self):
        """
        Test that the tasks:delete_task URL resolves to the view_task
        view
        """
        task = Task.objects.get(id=1)
        delete_task_url = reverse('tasks:delete_task', args=[task.id])
        # resolve(url).func = tasks.views.delete_task
        self.assertEqual(resolve(delete_task_url).func, delete_task)
