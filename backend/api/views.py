from django.shortcuts import render

import requests

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        return Response({"test": "get"})


class LikedTweetAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        user_id = "1365833961918722048"
        bearer_token: string = "AAAAAAAAAAAAAAAAAAAAADX3WQEAAAAAs2gl8fN4BgszWpN0l0wsaj2%2B19M%3D2kbvsTN7DDdRTAe2dlLnqDPGpNhBhZpzeC0kocaustllURW1cg"
        url: string = "https://api.twitter.com/2/users/{}/liked_tweets".format(user_id)
        header: dict = {"Authorization": "Beare {}".format(bearer_token)}

        response: requests.models.Response = requests.get(url=url, headers=header)
        return Response(response.json())
