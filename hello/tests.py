import pytest
from django.test import TestCase
from django.urls import reverse
from .models import Greeting

pytestmark = pytest.mark.django_db
# Create your tests here.

class HelloTest:

    def setUp(self):
        Greeting.objects.create(greeting='Yo')
        Greeting.objects.create(greeting='Hola')

    # Home
    # --------------
    def test_hello_view_returns_200(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)

    def test_hello_view_uses_correct_template(self):
        response = self.client.get(reverse('hello'))
        self.assertTemplateUsed(response, 'hello/base.html')

    def test_hello_view_response_contains(self):
        response = self.client.get(reverse('hello'))
        self.assertContains(response, 'Hello')

    def test_hello_view_response_not_contains(self):
        response = self.client.get(reverse('hello'))
        self.assertNotContains(response, 'Poop-Man')

    # Greetings
    # --------------
    def test_greeting_view_returns_200(self):
        response = self.client.get(reverse('greetings'))
        self.assertEqual(response.status_code, 200)

    def test_greeting_view_uses_correct_template(self):
        response = self.client.get(reverse('greetings'))
        self.assertTemplateUsed(response, 'hello/greetings.html')

    def test_greeting_view_response_contains(self):
        response = self.client.get(reverse('greetings'))
        self.assertContains(response, 'Yo')
        self.assertContains(response, 'Hola')

    def test_greeting_view_response_not_contains(self):
        response = self.client.get(reverse('greetings'))
        self.assertNotContains(response, 'Poop-Man')
        self.assertNotContains(response, 'Poop-Man2')
