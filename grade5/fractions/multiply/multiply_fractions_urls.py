from django.urls import path
from django.urls import path
from . import multiply_fractions_views

# URLConf
urlpatterns = [
    path('', multiply_fractions_views.fractions_multiply_page)
]
