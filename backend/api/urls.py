from django.urls import path

from .views import LikedTweetAPI

urlpatterns = [
    path(r"liked_tweet", LikedTweetAPI.as_view()),
]
