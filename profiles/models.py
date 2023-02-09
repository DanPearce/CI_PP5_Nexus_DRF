"""
Models for profiles
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This class is used to define the model parameters for profiles.
        - Defined as a One to One realtionship with the User model.
        - Model contents created as soon as a User is created.
    """
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    name = models.CharField(
        max_length=60,
        blank=True
        )
    about = models.TextField(
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
        default='../default_profile_besijt'
    )

    class Meta:
        """
        Ordering based on created_on time/date
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        This function returns the name of the user's profile
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Creates a profile once the User has been created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
