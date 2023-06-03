from django.urls import path
from django.urls import path
from . import divide_decimals_views

# URLConf
urlpatterns = [
    path('', divide_decimals_views.decimals_divide_page)
]
