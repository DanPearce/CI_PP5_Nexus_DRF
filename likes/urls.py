"""
Urls for likes
"""
# Imports Internal
from likes import views
# -----------------------------------------------------------------------
# Third Party
from django.urls import path

urlpatterns = [
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>', views.LikeDetail.as_view()),
]
