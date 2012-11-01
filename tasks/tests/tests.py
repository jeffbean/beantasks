"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from tasks.models import Task, Project
from django.contrib.auth.models import User
from django.test.client import Client

class TaskTestCase(unittest.TestCase):
    def setUp(self):
        """
        Create a simple client test base with minimum fields
        """
        self.client = Client()
        self.testuser = User.objects.create_user('testuser', 'test@example.com', 'start123')
        self.testuser2 = User.objects.create_user('test2', 'test2@example.com', 'start123')

        self.task = Task.objects.create(doer=self.testuser, task='testtask', priority=5)
        self.task2 = Task.objects.create(doer=self.testuser2, task='testtask2', notes='Testing Task2', priority=5)

        self.project = Project.objects.create(title='testproject', owner=self.testuser)
        self.project2 = Project.objects.create(title='testproject2', owner=self.testuser2)

    def tearDown(self):
        self.testuser.delete()
        self.testuser2.delete()
        self.task.delete()
        self.task2.delete()
        self.project.delete()
        self.project2.delete()

    def test_task_is_recently_published(self):
        """ Does the task return it was recently published """
        self.assertEqual(self.task.was_published_recently(), True)

    def test_task_add_under_project(self):
        """ Add task to project """
        self.task.project = self.project
        self.project.save()
        self.assertEqual(self.task.project, self.project)


    def test_project_is_recently_published(self):
        """ Does the task return it was recently published """
        self.assertEqual(self.project.was_published_recently(), True)

    def test_task_modify_time(self):
        """ If I edit task will modify time be greater than create time """
        self.task.task = 'create more testing'
        self.task.save()
        self.assertGreater(self.task.modified, self.task.created)

    def test_project_modify_time(self):
        """ If I edit project will modify time be greater than create time """
        self.project.title = 'create more testing'
        self.project.save()
        self.assertGreater(self.project.modified, self.project.created)

    def test_modify_task_user(self):
        """ Change the doer field (User obj) for a task """
        self.task.doer = self.testuser2
        self.task.save()
        self.assertEqual(self.task.doer, self.testuser2)

    def test_modify_project_user(self):
        """ Change the doer field (User obj) for a task """
        self.project.doer = self.testuser2
        self.project.save()
        self.assertEqual(self.project.doer, self.testuser2)

    def content_test(self, url, values):
        """Get content of url and test that each of items in `values` list is present."""
        r = self.client.get(url)
        self.assertEquals(r.status_code, 200)
        for v in values:
            self.assertTrue(v in r.content)

    def test_login_home(self):
        """ Login as test and go to homepage """
        self.client.login(username="testuser", password="start123")
        self.content_test("/", ['<title>Bean Tasks</title>', '<div id="content" class="span9">'])

