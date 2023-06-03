from django.urls import path
from django.urls import path
from . import multiply_decimals_views

# URLConf
urlpatterns = [
    path('', multiply_decimals_views.decimals_multiply_page)
]
