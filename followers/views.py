"""
Views for followers
"""
# Imports Internal
from .models import Follower
from .serializers import FollowerSerializer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework import generics, permissions


class FollowerList(generics.ListCreateAPIView):
    """
    Class based view for Follower List
    -   Lists all follows
    -   Allows for a follow to be created, if authenticated.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Class based view for Follower Detail
    -   Allows us to view the full follower detail.
    -   Allows the owner to delete the follow.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
