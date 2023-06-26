from django.urls import path
from django.urls import path, include
from . import grade5factoringviews

# URLConf
urlpatterns = [
    path('home/', grade5factoringviews.grade5_factoring_home),
    path('list/', include('grade5.factoring.list.grade5_factors_list_urls')),
    path('prime/', include('grade5.factoring.prime.grade5_factors_prime_urls')),
    path('gcf/', include('grade5.factoring.gcf.grade5_factors_gcf_urls')),
    path('lcm/', include('grade5.factoring.lcm.grade5_factors_lcm_urls')),
]
