"""
Tests for profiles. Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Profile

PASSWORD = secrets.token_urlsafe(18)


class ProfileTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password=PASSWORD)
        self.bob = User.objects.create_user('bob', password=PASSWORD)

    def test_a_profile_is_created_with_every_user(self):
        self.assertEqual(Profile.objects.count(), 2)

    def test_profiles_are_public(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 2)
        profile = Profile.objects.get(owner=self.alice)
        self.assertEqual(self.client.get(f'/profiles/{profile.id}').status_code, 200)

    def test_owner_can_edit_their_profile_but_nobody_else_can(self):
        profile = Profile.objects.get(owner=self.alice)
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.patch(f'/profiles/{profile.id}', {'name': 'Hacked'}).status_code, 403)
        self.client.force_authenticate(self.alice)
        self.assertEqual(self.client.patch(f'/profiles/{profile.id}', {'name': 'Alice A'}).status_code, 200)
        profile.refresh_from_db()
        self.assertEqual(profile.name, 'Alice A')
