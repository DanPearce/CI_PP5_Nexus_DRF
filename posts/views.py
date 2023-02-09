"""
Views for posts
"""
# Imports Internal
from .models import Post
from .serializers import PostSerializer
from ci_pp5_nexus_drf.permissions import IsOwnerOrReadOnly
# -----------------------------------------------------------------------
# Third Party
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.http import Http404


class PostList(APIView):
    """
    Class based view for Post List
    -   Lists all posts
    -   Allows a post to be created if authenticated
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PostDetail(APIView):
    """
    Class based view for Post Detail
    -   Allows us to see the full post detail
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        """
        Function to get post object by it id (Primary Key)
        """
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Function to return the serialized post data
        """
        post = self.get_object(pk)
        serializer = PostSerializer(
            post,
            context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Function to update post by its id
        """
        post = self.get_object(pk)
        serializer = PostSerializer(
            post,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Function to delete post by id
        """
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
