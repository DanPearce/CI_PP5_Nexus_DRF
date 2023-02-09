"""
Views for posts
"""
# Imports Internal
from .models import Post
from .serializers import PostSerializer
# -----------------------------------------------------------------------
# Third Party
from rest_framework.response import Response
from rest_framework.views import APIView


class PostList(APIView):
    """
    Class based view for Post List
    -   Lists all posts
    """
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
