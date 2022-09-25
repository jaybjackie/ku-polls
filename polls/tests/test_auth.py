"""Test for authentication."""
from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User


class UserAuthenticationTest(TestCase):
    """Test about authenticated user."""
    def setUp(self) -> None:
        self.auth = {
            'username': 'Jason',
            'password': 'JasonSoHandsome'
        }
        User.objects.create_user(**self.auth)

    def test_login_exist(self):
        """Access to login page"""
        response = self.client.get(reverse('login'))
        # check status code
        self.assertEqual(200, response.status_code)
