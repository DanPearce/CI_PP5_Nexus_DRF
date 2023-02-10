"""
Urls for posts
"""
# Imports Internal
from comments import views
# -----------------------------------------------------------------------
# Third Party
from django.urls import path

urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),
]
