"""
Serializers for profiles
"""
# Imports Internal
from .models import Profile
from followers.models import Follower
# -----------------------------------------------------------------------
# Third Party
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Profile data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Function to check if user is owner
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Function to check if authenticated user is following other users.
        -   Populates id if logged in & following.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'about', 'created_on', 'updated_on',
            'image', 'is_owner', 'following_id', 'posts_count',
            'following_count', 'followers_count',
        ]
