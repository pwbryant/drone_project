from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class HelloTest(TestCase):

    def test_view_returns_200(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('hello'))
        self.assertTemplateUsed(response, 'hello/base.html')

    def test_view_response_contains(self):
        response = self.client.get(reverse('hello'))
        self.assertContains(response, 'Hello')

    def test_view_response_not_contains(self):
        response = self.client.get(reverse('hello'))
        self.assertNotContains(response, 'Poop-Man')
