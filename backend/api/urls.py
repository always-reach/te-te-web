from django.urls import path

from .views import TestAPI, LikedTweetAPI, CreateAuthenticateEndpoint

urlpatterns = [
    path(r"test", TestAPI.as_view(), name="detail"),
    path(r"auth_twitter",CreateAuthenticateEndpoint.as_view()),
    path(r"liked_tweet", LikedTweetAPI.as_view())
]
