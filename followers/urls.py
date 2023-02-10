"""
Urls for followers
"""
# Imports Internal
from followers import views
# -----------------------------------------------------------------------
# Third Party
from django.urls import path

urlpatterns = [
    path('followers/', views.FollowerList.as_view()),
    path('followers/<int:pk>', views.FollowerDetail.as_view()),
]
