"""
Serializers for profiles
"""
# Imports Internal
from .models import Profile
# -----------------------------------------------------------------------
# Third Party
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    """
    Class based serializer for Profile data
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Function to check if user is owner
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'about', 'created_on', 'updated_on',
            'image', 'is_owner',
        ]
