"""
Urls for posts
"""
# Imports Internal
from posts import views
# -----------------------------------------------------------------------
# Third Party
from django.urls import path

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
]
