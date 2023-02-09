"""
Admin view for profiles
"""
# Imports Internal
from .models import Profile
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin


admin.site.register(Profile)
