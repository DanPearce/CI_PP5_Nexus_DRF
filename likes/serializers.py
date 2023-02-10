"""
Serializers for likes
"""
# Imports
from .models import Like
# -----------------------------------------------------------------------
# Third Party
from django.db import IntegrityError
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Like data
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post', 'created_on'
        ]

    def create(self, validated_data):
        """
        Function to handle duplication of likes.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Possible duplicate like'
            })
