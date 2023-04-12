from django.urls import path
from django.urls import path
from . import timeviews

# URLConf
urlpatterns = [
    path('', timeviews.time_page)
]
