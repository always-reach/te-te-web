from django.urls import path

from .views import TestAPI

urlpatterns = [
    path(r"test", TestAPI.as_view(),name="detail")
]
