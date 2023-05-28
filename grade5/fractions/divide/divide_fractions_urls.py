from django.urls import path
from django.urls import path
from . import divide_fractions_views

# URLConf
urlpatterns = [
    path('', divide_fractions_views.fractions_divide_page)
]
