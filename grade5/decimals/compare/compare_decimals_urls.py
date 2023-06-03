from django.urls import path
from django.urls import path
from . import compare_decimals_views

# URLConf
urlpatterns = [
    path('', compare_decimals_views.decimals_compare_page)
]
