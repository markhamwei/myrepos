from django.urls import path
from django.urls import path
from . import simplify_fractions_views

# URLConf
urlpatterns = [
    path('', simplify_fractions_views.fractions_simplily_page)
]
