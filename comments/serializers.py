"""
Serializers for comments
"""
# Imports Internal
from .models import Comment
# -----------------------------------------------------------------------
# Third Party
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Comment data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    updated_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to check if user is owner
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        """
        Function to get the humanized time for created_on
        """
        return naturaltime(obj.created_on)

    def get_updated_on(self, obj):
        """
        Function to get the humanized time for updated_on
        """
        return naturaltime(obj.updated_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'post', 'created_on', 'updated_on', 'body',
            'is_owner', 'profile_id', 'profile_image'
        ]


class CommentDetailSerlizer(CommentSerializer):
    """
    Class based serialiser for the comment model, in detail view
    """
    post = serializers.ReadOnlyField(source='post.id')
