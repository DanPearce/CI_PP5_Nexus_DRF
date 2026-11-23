"""
Tests for the API as a whole: the welcome route, registration, login cookies, logout and CORS.
Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from django.conf import settings
from django.test import override_settings
from rest_framework import status
from rest_framework.test import APITestCase

from profiles.models import Profile

# Fresh random passwords for every test run: no password literals in the repository
PASSWORD = secrets.token_urlsafe(18)
AUTH_COOKIE = settings.REST_AUTH['JWT_AUTH_COOKIE']
REFRESH_COOKIE = settings.REST_AUTH['JWT_AUTH_REFRESH_COOKIE']


class RootAndAuthTests(APITestCase):
    def test_welcome_message(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', response.json()['message'])

    def test_registration_creates_a_user_and_a_profile(self):
        response = self.client.post('/dj-rest-auth/registration/', {
            'username': 'newbie', 'password1': PASSWORD, 'password2': PASSWORD})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Profile.objects.filter(owner__username='newbie').exists())

    def test_registration_rejects_mismatched_passwords(self):
        response = self.client.post('/dj-rest-auth/registration/', {
            'username': 'newbie', 'password1': PASSWORD, 'password2': PASSWORD + 'x'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username='newbie').exists())

    def test_login_sets_secure_http_only_cookies_and_unlocks_the_user_endpoint(self):
        User.objects.create_user('alice', password=PASSWORD)
        self.assertEqual(self.client.get('/dj-rest-auth/user/').status_code, 401)
        response = self.client.post('/dj-rest-auth/login/', {'username': 'alice', 'password': PASSWORD})
        self.assertEqual(response.status_code, 200)
        for name in (AUTH_COOKIE, REFRESH_COOKIE):
            with self.subTest(cookie=name):
                cookie = response.cookies[name]
                self.assertTrue(cookie['secure'])
                self.assertTrue(cookie['httponly'])
                self.assertEqual(cookie['samesite'], 'None')
        user = self.client.get('/dj-rest-auth/user/')
        self.assertEqual(user.status_code, 200)
        self.assertEqual(user.json()['username'], 'alice')

    def test_wrong_password_is_rejected(self):
        User.objects.create_user('alice', password=PASSWORD)
        response = self.client.post('/dj-rest-auth/login/', {'username': 'alice', 'password': PASSWORD + 'x'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertNotIn(AUTH_COOKIE, response.cookies)

    def test_logout_expires_both_cookies(self):
        response = self.client.post('/dj-rest-auth/logout/')
        self.assertEqual(response.status_code, 200)
        for name in (AUTH_COOKIE, REFRESH_COOKIE):
            with self.subTest(cookie=name):
                self.assertEqual(response.cookies[name]['max-age'], 0)
                self.assertEqual(response.cookies[name].value, '')


@override_settings(CORS_ALLOWED_ORIGINS=['https://nexus.example'], CORS_ALLOW_CREDENTIALS=True)
class CorsTests(APITestCase):
    def test_the_front_end_origin_is_allowed_with_credentials(self):
        response = self.client.options('/posts/', HTTP_ORIGIN='https://nexus.example',
                                       HTTP_ACCESS_CONTROL_REQUEST_METHOD='GET')
        self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), 'https://nexus.example')
        self.assertEqual(response.headers.get('Access-Control-Allow-Credentials'), 'true')

    def test_another_origin_is_not_allowed(self):
        response = self.client.options('/posts/', HTTP_ORIGIN='https://evil.example',
                                       HTTP_ACCESS_CONTROL_REQUEST_METHOD='GET')
        self.assertNotIn('Access-Control-Allow-Origin', response.headers)
