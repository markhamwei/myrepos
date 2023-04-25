from django.urls import path
from django.urls import path
from . import identify_fractions_views

# URLConf
urlpatterns = [
    path('', identify_fractions_views.fractions_identify_page)
]
