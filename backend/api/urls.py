from django.urls import path

from .views import TestAPI, LikedTweetAPI

urlpatterns = [
    path(r"test", TestAPI.as_view(), name="detail"),
    path(r"liked_tweet", LikedTweetAPI.as_view())
]
