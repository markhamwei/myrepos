from django.urls import path
from django.urls import path
from . import perimeterviews

# URLConf
urlpatterns = [
    path('', perimeterviews.perimeter_page)
]
