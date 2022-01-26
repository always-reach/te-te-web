import requests
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings

from .util import format_twitter_response


class LikedTweetAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        print(request.GET)
        user_id: str = request.GET.get("id")
        url: str = settings.TWITTER_URL + "users/" + user_id + "/liked_tweets"
        headers: dict = {"Authorization": "Bearer {}".format(settings.TWITTER_BEARER_TOKEN)}
        params: dict = {"expansions": 'author_id,attachments.media_keys',
                        'media.fields': 'url',
                        'place.fields': 'country,country_code',
                        'tweet.fields': 'created_at,lang',
                        'user.fields': 'created_at,description,id,name'
                        }
        response: Response = requests.request(method="GET", url=url, headers=headers, params=params)
        formate_response = format_twitter_response(response.json())
        if response.status_code == 200:
            return Response(formate_response)
        else:
            return Response({"status_code": response.status_code})
