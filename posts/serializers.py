"""
Serializers for posts
"""
# Imports Internal
from .models import Post
from likes.models import Like
# -----------------------------------------------------------------------
# Third Party
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Post data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
        )
    like_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to check if user is owner
        """
        request = self.context['request']
        return request.user == obj.owner

    def validate_image(self, value):
        """
        Function to check image width/height and size
        """
        PIXELS = 3840
        FILE_LIMIT = 3

        if value.image.height > PIXELS:
            raise serializers.ValidationError(
                f'Sorry, the image height is larger than {PIXELS} pixels.'
            )

        if value.image.width > PIXELS:
            raise serializers.ValidationError(
                f'Sorry, the image width is larger than {PIXELS} pixels.'
            )

        if value.size > 1024 * 1024 * FILE_LIMIT:
            raise serializers.ValidationError(
                f'Sorry, the image size is larger than {FILE_LIMIT} MB.'
            )

    def get_like_id(self, obj):
        """
        Function to check if authenticated user liked a post.
        -   Populates id if logged in & liked.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'body', 'created_on', 'updated_on',
            'image', 'is_owner', 'profile_id', 'profile_image', 'like_id',
        ]
