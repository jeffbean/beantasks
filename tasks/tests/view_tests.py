"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from tasks.models import Task, Project

class ViewTestCases(unittest.TestCase):
    urls = 'tasks.urls'

    def setUp(self):
        """
        Create a simple client test base with minimum fields
        """
        self.client = Client()

    def tearDown(self):
        pass

    def test_index(self):
        """ goto index view make sure it loads """
        self.client.get('/')
