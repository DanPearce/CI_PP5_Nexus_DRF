"""
Serializers for followers
"""
# Imports Internal
from .models import Follower
# -----------------------------------------------------------------------
# Third Party
from django.db import IntegrityError
from rest_framework import serializers


class FollowerSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Follower data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'followed', 'created_on', 'followed_name'
        ]

    def create(self, validated_data):
        """
        Function to handle duplication of follows.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplicate follow.'
            })
