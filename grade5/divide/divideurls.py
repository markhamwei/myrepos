from django.urls import path
from django.urls import path
from . import divideviews

# URLConf
urlpatterns = [
    path('', divideviews.divide_page)
]
