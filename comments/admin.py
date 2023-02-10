"""
Admin view for posts
"""
# Imports Internal
from .models import Comment
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin

admin.site.register(Comment)