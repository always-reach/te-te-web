from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class TestAPI(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        return Response({"test": "get"})
