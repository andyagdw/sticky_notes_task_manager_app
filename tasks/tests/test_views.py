"""
Unit testing task views in the tasks app

This module contains a test case class 'TestViews' which inherits from
Django's 'TestCase'. The class contains various tests to ensure the
correct behaviour of the task views
"""
# tasks/tests

import datetime
from django.test import Client, TestCase
from django.urls import reverse
from tasks.models import Task


class TestViews(TestCase):
    """
    A subclass which inherits from Testcase

    It contains six tests that verify the correct behaviour of task
    views
    """

    def setUp(self) -> None:
        """Set up the client and create a sample task for testing"""
        self.client = Client()
        self.current_date = datetime.date.today()
        self.tomorrow_date = (
            datetime.date.today() + datetime.timedelta(days=1)
            )

        self.task = Task.objects.create(
            title="My task",
            description="My new task",
            category="My new task",
            deadline=self.current_date,
            priority=1,
        )

        self.index_url = reverse('tasks:index')
        self.view_task_url = (
            reverse('tasks:view_task', args=[self.task.id])
            )
        self.edit_task_url = (
            reverse('tasks:edit_task', args=[self.task.id])
            )
        self.delete_task_url = (
            reverse('tasks:delete_task', args=[self.task.id])
            )

    def test_index_request_method_get(self):
        """
        Test that the index view returns a 200 status and uses the
        correct template
        """
        response = self.client.get(self.index_url)
        # HTTP 200 OK success status response code
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_adds_new_task_request_method_post(self):
        """Test that a new task can be added via a POST request to the
        index view"""

        new_task_title = 'Shopping'
        new_task_description = "Purchase items from the grocery list"
        new_task_category = 'Shopping'
        new_task_deadline = self.tomorrow_date
        new_task_priority = 2

        # Creates a new task instance
        response = self.client.post(self.index_url, {
            'title': new_task_title,
            'description': new_task_description,
            'category': new_task_category,
            'deadline': new_task_deadline,
            'priority': new_task_priority,
        })

        # Get recently created task
        new_task = Task.objects.latest('id')

        # HTTP 302 Redirect status code
        self.assertEqual(response.status_code, 302)
        self.assertEqual(new_task.title, new_task_title)
        self.assertEqual(new_task.description, new_task_description)
        self.assertEqual(new_task.category, new_task_category)
        self.assertEqual(new_task.deadline, new_task_deadline)
        self.assertEqual(new_task.priority, new_task_priority)

    def test_view_task_request_method_get(self):
        """
        Test that the view task view returns a 200 status and uses
        the correct template
        """
        response = self.client.get(self.view_task_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_task.html')

    def test_edit_task_request_method_get(self):
        """
        Test that the edit task view returns a 200 status and uses the
        correct template"""
        response = self.client.get(self.edit_task_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_task.html')

    def test_edit_task_request_method_post(self):
        """
        Test that an existing task can be edited via a POST request
        to the edit task view
        """

        edit_form_data = {
            'title': 'Updated task',
            'description': 'Updated description',
            'category': 'Updated category',
            'deadline': self.current_date,
            'priority': 2,
        }

        response = self.client.post(self.edit_task_url,
                                    data=edit_form_data)

        self.assertRedirects(response, self.view_task_url)

        updated_task = Task.objects.get(id=1)
        # Use '.title()' as this is how I save title to the database
        (self.assertEqual(updated_task.title,
                          edit_form_data['title'].title()))
        (self.assertEqual(updated_task.description,
                          edit_form_data['description']))
        # Use '.title()' as this is how I save category to the database
        (self.assertEqual(updated_task.category,
                          edit_form_data['category'].title()))
        self.assertEqual(updated_task.deadline, edit_form_data['deadline'])
        self.assertEqual(updated_task.priority, edit_form_data['priority'])

    def test_delete_task_request_method_post(self):
        """
        Test that an existing task can be deleted via a POST request
        to the delete task view
        """
        response = self.client.post(self.delete_task_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)
