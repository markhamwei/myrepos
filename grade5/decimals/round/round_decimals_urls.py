from django.urls import path
from django.urls import path
from . import round_decimals_views

# URLConf
urlpatterns = [
    path('', round_decimals_views.decimals_round_page)
]
