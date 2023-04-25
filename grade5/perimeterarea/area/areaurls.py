from django.urls import path
from django.urls import path
from . import areaviews

# URLConf
urlpatterns = [
    path('', areaviews.area_page)
]
