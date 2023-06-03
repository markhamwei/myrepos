from django.urls import path
from django.urls import path
from . import subtractviews

# URLConf
urlpatterns = [
    path('', subtractviews.subtract_page)
]
