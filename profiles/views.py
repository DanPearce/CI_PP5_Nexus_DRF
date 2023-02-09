"""
Views for profiles
"""
# Imports Internal 
from .models import Profile
# -----------------------------------------------------------------------
# Third Party
from rest_framework.views import APIView
from rest_framework.response import Response


class ProfileList(APIView):
    """
    Class based view for Profile List
    -   Lists all profiles
    """
