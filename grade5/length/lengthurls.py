from django.urls import path
from django.urls import path
from . import lengthviews

# URLConf
urlpatterns = [
    path('', lengthviews.length_page)
]
