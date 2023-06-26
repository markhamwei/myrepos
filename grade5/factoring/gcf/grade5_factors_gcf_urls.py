from django.urls import path
from django.urls import path
from . import grade5_factors_gcf_views

# URLConf
urlpatterns = [
    path('', grade5_factors_gcf_views.grade5_factors_gcf_page)
]
