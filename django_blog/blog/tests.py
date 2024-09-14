from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

class AuthenticationTestCase(TestCase):
    def test_user_registration(self):
        response = self.client.post('/register/', {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirection after successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'testpassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirection after successful login

    def test_profile_update(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')
        response = self.client.post('/profile/', {
            'username': 'updateduser',
            'email': 'updated@example.com'
        })
        self.assertEqual(response.status_code, 200)
        user.refresh_from_db()
        self.assertEqual(user.username, 'updateduser')
        self.assertEqual(user.email, 'updated@example.com')
