"""
Views for profiles
"""
# Imports Internal
from .models import Profile
from .serializers import ProfileSerializer
# -----------------------------------------------------------------------
# Third Party
from rest_framework.views import APIView
from rest_framework.response import Response


class ProfileList(APIView):
    """
    Class based view for Profile List
    -   Lists all profiles
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
