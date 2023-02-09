"""
Serializers for posts
"""
# Imports Internal
from posts.models import Post
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
        soruce='owner.profile.image.url'
        )

    def get_is_owner(self, obj):
        """
        Function to check if user is owner
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'body', 'created_on', 'updated_on',
            'image', 'is_owner', 'profile_id', 'profile_image',
        ]
