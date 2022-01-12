from django.shortcuts import render

import requests
from requests_oauthlib import OAuth2Session

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        return Response({"test": "get"})


class CreateAuthenticateEndpoint(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        twitter = OAuth2Session(client_id=CLIENT_ID)
        authorization_url, state = twitter.authorization_url()
        print(authorization_url, state)
        return Response({"test": "hoge"})


class LikedTweetAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        oauth = OAuth2Session()
        url: str = "https://api.twitter.com/2/users/{}/liked_tweets".format(user_id)
        header: dict = {"Authorization": "Beare {}".format(bearer_token)}

        response: requests.models.Response = requests.get(url=url, headers=header)
        return Response(response.json())
