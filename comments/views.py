"""
Views for comments
"""
# Imports Internal
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerlizer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend


class CommentList(generics.ListCreateAPIView):
    """
    Class based view for Comment List
    -   Lists all comments
    -   Allows for a comment to be created, if authenticated
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class based view for Comment Detail
    -   Allows us to view full comment detail
    -   Allows owner to modify or delete.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerlizer
    queryset = Comment.objects.all()
