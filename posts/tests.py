"""
Tests for posts: public reading, sign-in to post, and only the owner can change or delete.
Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from .models import Post

PASSWORD = secrets.token_urlsafe(18)


class PostTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password=PASSWORD)
        self.bob = User.objects.create_user('bob', password=PASSWORD)
        self.post = Post.objects.create(owner=self.alice, title='First post', body='Hello')

    def test_anyone_can_read_posts(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['count'], 1)
        self.assertEqual(self.client.get(f'/posts/{self.post.id}').status_code, 200)

    def test_missing_post_is_404(self):
        self.assertEqual(self.client.get('/posts/9999').status_code, 404)

    def test_posting_needs_sign_in(self):
        response = self.client.post('/posts/', {'title': 'Nope', 'body': 'x'})
        self.assertIn(response.status_code, (401, 403))
        self.assertEqual(Post.objects.count(), 1)

    def test_signed_in_user_can_post_and_becomes_the_owner(self):
        self.client.force_authenticate(self.bob)
        response = self.client.post('/posts/', {'title': 'Bob here', 'body': 'Hi'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Post.objects.get(title='Bob here').owner, self.bob)

    def test_owner_can_edit_and_delete(self):
        self.client.force_authenticate(self.alice)
        self.assertEqual(self.client.patch(f'/posts/{self.post.id}', {'title': 'Edited'}).status_code, 200)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Edited')
        self.assertEqual(self.client.delete(f'/posts/{self.post.id}').status_code, 204)
        self.assertFalse(Post.objects.exists())

    def test_other_users_cannot_edit_or_delete(self):
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.patch(f'/posts/{self.post.id}', {'title': 'Hacked'}).status_code, 403)
        self.assertEqual(self.client.delete(f'/posts/{self.post.id}').status_code, 403)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'First post')

    def test_anonymous_cannot_edit_or_delete(self):
        self.assertIn(self.client.delete(f'/posts/{self.post.id}').status_code, (401, 403))
        self.assertTrue(Post.objects.exists())
