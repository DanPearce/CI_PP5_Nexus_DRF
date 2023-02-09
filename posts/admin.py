"""
Admin view for posts
"""
# Imports Internal
from .models import Post
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin

admin.site.register(Post)
