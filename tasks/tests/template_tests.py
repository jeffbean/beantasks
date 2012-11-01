"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from tasks.models import Task, Project
from django.template.loader import render_to_string
from django.forms.widgets import PasswordInput

class TemplateTestCases(unittest.TestCase):
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
        self.project2.delete(
                             )
    def index_template(self):

        with self.assertTemplateUsed(template_name='index.html'):
            render_to_string('index.html')

    def login_template(self):
        return
        self.assertFieldOutput(PasswordInput, {'start13': 'asdfasdf'}, {'': [u'Enter a valid password address.']})

