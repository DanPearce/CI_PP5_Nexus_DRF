"""
Views for profiles
"""
# Imports Internal
from .models import Profile
from .serializers import ProfileSerializer
# -----------------------------------------------------------------------
# Third Party
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


class ProfileList(APIView):
    """
    Class based view for Profile List
    -   Lists all profiles
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)


class ProfileDetail(APIView):
    """
    Class based view for Profile Detail
    -   Lists a user's profile
    """
    serializer_class = ProfileSerializer

    def get_object(self, pk):
        """
        Function to get profile object by its id (Primary Key)
        """
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Function to return serialized profile data
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Function to update a profile by its id
        """
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
