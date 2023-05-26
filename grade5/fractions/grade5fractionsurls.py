from django.urls import path
from django.urls import path, include
from . import grade5fractionsviews

# URLConf
urlpatterns = [
    path('home/', grade5fractionsviews.grade5_fractions_home),
    path('identify/', include('grade5.fractions.identify_fraction.identify_fractions_urls')),
    path('simplify/', include('grade5.fractions.simplify.simplify_fractions_urls')),
    path('addition/', include('grade5.fractions.addition.addition_fractions_urls'))
]
