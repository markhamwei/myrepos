from django.urls import path
from django.urls import path
from . import addition_decimals_views

# URLConf
urlpatterns = [
    path('', addition_decimals_views.decimals_addition_page)
]
