from django.urls import path, include
from . import volumeviews

# URLConf
urlpatterns = [
    path('', volumeviews.volume_page),
]
