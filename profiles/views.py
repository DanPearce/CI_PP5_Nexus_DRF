"""
Views for profiles
"""
# Imports Internal
from .models import Profile
from .serializers import ProfileSerializer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework import generics


class ProfileList(generics.ListAPIView):
    """
    Class based view for Profile List
    -   Lists all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Class based view for Profile Detail
    -   Allows us to see the full profile detail
    -   Allows us to modify a profile if authenticated.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
