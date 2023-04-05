from django.urls import path
from django.urls import path
from . import additionviews

# URLConf
urlpatterns = [
    path('', additionviews.addition_page)
]
