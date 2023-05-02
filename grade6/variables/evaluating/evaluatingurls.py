from django.urls import path
from django.urls import path
from . import evaluatingviews

urlpatterns = [
    path('', evaluatingviews.evaluating_page)
]