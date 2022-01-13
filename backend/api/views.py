import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings


class LikedTweetAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        print(request.GET)
        user_id: str = request.GET.get("id")
        url: str = settings.TWITTER_URL + "users/" + user_id + "/liked_tweets"
        headers: dict = {"Authorization": "Bearer {}".format(settings.TWITTER_BEARER_TOKEN)}
        response: Response = requests.request(method="GET", url=url, headers=headers)
        if response.status_code == 200:
            return Response(response.json())
        else:
            return Response({"status_code": response.status_code})
