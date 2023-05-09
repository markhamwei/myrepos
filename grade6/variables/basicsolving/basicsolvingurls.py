from django.urls import path
from django.urls import path
from . import basicsolvingviews

urlpatterns = [
    path('', basicsolvingviews.basicsolving_page)
]