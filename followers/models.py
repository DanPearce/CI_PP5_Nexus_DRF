"""
Models for followers
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    This class is used to define the model parameters for followers.
    -   Directly related to User and 'followed' User
    """
    owner = models.ForeignKey(
        User,
        related_name='following',
        on_delete=models.CASCADE
        )
    followed = models.ForeignKey(
        User,
        related_name='followed',
        on_delete=models.CASCADE
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """
        Ordering based on created_on time/date
        -   'unique_together' is used to prevent duplication of follows
        """
        ordering = ['-created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        This function returns which user has followed another
        """
        return f'{self.owner} followed {self.followed}'
