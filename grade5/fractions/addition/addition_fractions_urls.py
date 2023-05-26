from django.urls import path
from django.urls import path
from . import addition_fractions_views

# URLConf
urlpatterns = [
    path('', addition_fractions_views.fractions_addition_page)
]
