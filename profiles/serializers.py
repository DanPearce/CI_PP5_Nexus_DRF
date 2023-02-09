"""
Serializers for profiles
"""
# Imports Internal
from .models import Profile
# -----------------------------------------------------------------------
# Third Party
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'about', 'created_on', 'updated_on',
            'image'
        ]
