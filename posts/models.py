"""
Models for posts
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    This class is used to define the model parameters for posts.
        - Post is related to owner, the user.
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
        )
    title = models.CharField(
        max_length=225
        )
    body = models.TextField(
        blank=True
        )
    created_on = models.DateTimeField(
        auto_now_add=True
        )
    updated_on = models.DateTimeField(
        auto_now=True
        )
    image = models.ImageField(
        upload_to='images/',
        blank=True
    )

    class Meta:
        """
        Ordering based on created_on time/date
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        This function returns the post's title and owner
        """
        return f"{self.owner} - {self.title}"
