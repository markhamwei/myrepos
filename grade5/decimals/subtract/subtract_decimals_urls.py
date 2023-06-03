from django.urls import path
from django.urls import path
from . import subtract_decimals_views

# URLConf
urlpatterns = [
    path('', subtract_decimals_views.decimals_subtract_page)
]
