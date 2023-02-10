"""
Views for posts
"""
# Imports Internal
from .models import Post
from .serializers import PostSerializer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework import generics, permissions


class PostList(generics.ListCreateAPIView):
    """
    Class based view for Post List
    -   Lists all posts
    -   Allows a post to be created if authenticated
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class based view for Post Detail
    -   Allows us to see the full post detail
    -   Allows us to modify or delete a post if authenticated.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
