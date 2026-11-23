"""
Tests for followers. Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Follower

PASSWORD = secrets.token_urlsafe(18)


class FollowerTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password=PASSWORD)
        self.bob = User.objects.create_user('bob', password=PASSWORD)

    def test_following_needs_sign_in(self):
        response = self.client.post('/followers/', {'followed': self.alice.id})
        self.assertIn(response.status_code, (401, 403))
        self.assertEqual(Follower.objects.count(), 0)

    def test_follow_once_and_only_once(self):
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.post('/followers/', {'followed': self.alice.id}).status_code, 201)
        self.assertEqual(self.client.post('/followers/', {'followed': self.alice.id}).status_code, 400)
        self.assertEqual(Follower.objects.count(), 1)

    def test_only_the_follower_can_unfollow(self):
        follow = Follower.objects.create(owner=self.bob, followed=self.alice)
        self.client.force_authenticate(self.alice)
        self.assertEqual(self.client.delete(f'/followers/{follow.id}').status_code, 403)
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.delete(f'/followers/{follow.id}').status_code, 204)
