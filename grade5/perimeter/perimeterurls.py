from django.urls import path
from django.urls import path
from . import timeviews

# URLConf
urlpatterns = [
    path('', perimeterviews.perimeter_page)
]
