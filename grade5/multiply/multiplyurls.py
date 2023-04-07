from django.urls import path
from django.urls import path
from . import multiplyviews

# URLConf
urlpatterns = [
    path('', multiplyviews.multiply_page)
]
