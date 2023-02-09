"""
Permissions for nexus_drf
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission class to check a user is authenticated to make changes.
    """
    def has_object_permission(self, request, view, obj):
        """
        Function to check User for read only permissions or modify perms
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
