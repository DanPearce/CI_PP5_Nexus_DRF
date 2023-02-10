"""
Models for likes
"""
# Imports
from posts.models import Post
# -----------------------------------------------------------------------
# Third Party
from django.db import models
from django.contrib.auth.models import User


class Like(models.Model):
    """
    This class is used to define the model parameters for likes.
    -   Directly related to User and post
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    post = models.ForeignKey(
        Post,
        related_name='likes',
        on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Ordering based on created_on time/date
        -   'unique_together' is used to prevent duplication of likes
        """
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        """
        This function returns the which post a user has liked
        """
        return f'{self.owner} has liked {self.post}'
