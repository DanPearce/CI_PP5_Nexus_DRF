"""
Urls for profiles
"""
# Imports Internal
from profiles import views
# -----------------------------------------------------------------------
# Third Party
from django.urls import path

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]
