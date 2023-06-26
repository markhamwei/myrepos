from django.urls import path
from django.urls import path
from . import grade5_factors_lcm_views

# URLConf
urlpatterns = [
    path('', grade5_factors_lcm_views.grade5_factors_lcm_page)
]
