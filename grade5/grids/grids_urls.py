from django.urls import path
from django.urls import path
from . import grids_views

# URLConf
urlpatterns = [
    path('', grids_views.grids_page)
]
