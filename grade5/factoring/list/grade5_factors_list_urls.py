from django.urls import path
from django.urls import path
from . import grade5_factors_list_views

# URLConf
urlpatterns = [
    path('', grade5_factors_list_views.grade5_factors_list_page)
]
