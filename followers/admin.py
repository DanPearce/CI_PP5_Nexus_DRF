"""
Admin view for followers
"""
# Imports Internal
from .models import Follower
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin

admin.site.register(Follower)
