"""
Admin view for likes
"""
# Imports Internal
from .models import Like
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin

admin.site.register(Like)
