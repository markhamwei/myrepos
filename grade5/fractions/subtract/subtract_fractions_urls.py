from django.urls import path
from django.urls import path
from . import subtract_fractions_views

# URLConf
urlpatterns = [
    path('', subtract_fractions_views.fractions_subtract_page)
]
