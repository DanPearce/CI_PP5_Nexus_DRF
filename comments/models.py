"""
Models for comments
"""
# Imports Internal
from posts.models import Post
# -----------------------------------------------------------------------
# Third Party
from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    """
    This class based model is used to define the parameters for a comment.
    -   Directly related to User and Post
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    body = models.TextField()

    class Meta:
        """
        Ordering based on created_on time/date
        """
        ordering = ['created_on']

    def __str__(self):
        """
        This function returns the comment's body content
        """
        return self.body
