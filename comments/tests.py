"""
Tests for comments. Run with:  SECRET_KEY=test python manage.py test
"""
import secrets

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from posts.models import Post
from .models import Comment

PASSWORD = secrets.token_urlsafe(18)


class CommentTests(APITestCase):
    def setUp(self):
        self.alice = User.objects.create_user('alice', password=PASSWORD)
        self.bob = User.objects.create_user('bob', password=PASSWORD)
        self.post = Post.objects.create(owner=self.alice, title='A post', body='Hello')
        self.comment = Comment.objects.create(owner=self.alice, post=self.post, body='First!')

    def test_anyone_can_read_and_filter_by_post(self):
        other = Post.objects.create(owner=self.bob, title='Another', body='x')
        Comment.objects.create(owner=self.bob, post=other, body='Elsewhere')
        response = self.client.get(f'/comments/?post={self.post.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual([c['body'] for c in response.json()['results']], ['First!'])

    def test_commenting_needs_sign_in(self):
        response = self.client.post('/comments/', {'post': self.post.id, 'body': 'hi'})
        self.assertIn(response.status_code, (401, 403))
        self.assertEqual(Comment.objects.count(), 1)

    def test_signed_in_user_can_comment(self):
        self.client.force_authenticate(self.bob)
        response = self.client.post('/comments/', {'post': self.post.id, 'body': 'Nice'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.get(body='Nice').owner, self.bob)

    def test_only_the_owner_can_edit_or_delete(self):
        self.client.force_authenticate(self.bob)
        self.assertEqual(self.client.patch(f'/comments/{self.comment.id}', {'body': 'x'}).status_code, 403)
        self.assertEqual(self.client.delete(f'/comments/{self.comment.id}').status_code, 403)
        self.client.force_authenticate(self.alice)
        self.assertEqual(self.client.patch(f'/comments/{self.comment.id}', {'body': 'Edited'}).status_code, 200)
        self.assertEqual(self.client.delete(f'/comments/{self.comment.id}').status_code, 204)
