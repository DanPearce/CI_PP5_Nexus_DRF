"""
Urls for nexus_drf
"""
# Imports
# -----------------------------------------------------------------------
# Third Party
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
