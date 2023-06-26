from django.urls import path
from django.urls import path
from . import grade5_factors_prime_views

# URLConf
urlpatterns = [
    path('', grade5_factors_prime_views.grade5_factors_prime_page)
]
