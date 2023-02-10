"""
Views for comments
"""
# Imports Internal
from .models import Like
from .serializers import LikeSerializer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework import generics, permissions


class LikeList(generics.ListCreateAPIView):
    """
    Class based view for Like List
    -   Lists all comments
    -   Allows for a like to be created, if authenticated
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Class based view for Like Detail
    -   Allows us to view full like detail
    -   Allows owner to delete.
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
