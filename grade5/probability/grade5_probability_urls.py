from django.urls import path
from django.urls import path, include
from . import grade5_probability_views

# URLConf
urlpatterns = [
    path('home/', grade5_probability_views.grade5_probability_home),
    path('spinner/', include('grade5.probability.spinner.grade5_probability_spinner_urls')),
    path('prime/', include('grade5.factoring.prime.grade5_factors_prime_urls')),
    path('gcf/', include('grade5.factoring.gcf.grade5_factors_gcf_urls')),
    path('lcm/', include('grade5.factoring.lcm.grade5_factors_lcm_urls')),
]
