"""
Tests for likes. Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from posts.models import Post
from .models import Like

PASSWORD = secrets.token_urlsafe(18)


class LikeTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password=PASSWORD)
        self.bob = User.objects.create_user('bob', password=PASSWORD)
        self.post = Post.objects.create(owner=self.alice, title='A post', body='Hello')

    def test_liking_needs_sign_in(self):
        response = self.client.post('/likes/', {'post': self.post.id})
        self.assertIn(response.status_code, (401, 403))
        self.assertEqual(Like.objects.count(), 0)

    def test_a_post_can_only_be_liked_once_per_user(self):
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.post('/likes/', {'post': self.post.id}).status_code, 201)
        self.assertEqual(self.client.post('/likes/', {'post': self.post.id}).status_code, 400)
        self.assertEqual(Like.objects.count(), 1)

    def test_only_the_owner_can_unlike(self):
        like = Like.objects.create(owner=self.bob, post=self.post)
        self.client.force_authenticate(self.alice)
        self.assertEqual(self.client.delete(f'/likes/{like.id}').status_code, 403)
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.delete(f'/likes/{like.id}').status_code, 204)
        self.assertFalse(Like.objects.exists())
