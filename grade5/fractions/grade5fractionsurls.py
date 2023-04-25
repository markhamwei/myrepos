from django.urls import path
from django.urls import path, include
from . import grade5fractionsviews

# URLConf
urlpatterns = [
    path('home/', grade5fractionsviews.grade5_fractions_home),
    path('identify/', include('grade5.fractions.identify_fraction.identify_fractions_urls'))
]
