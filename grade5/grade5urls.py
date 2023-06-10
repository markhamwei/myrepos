from django.urls import path
from django.urls import path, include
from . import grade5views

# URLConf
urlpatterns = [
    path('home/', grade5views.grade5_home),
    path("wholenumbers/", include('grade5.wholenumbers.grade5wholenumbersurls')),
    path("length/", include('grade5.length.lengthurls')),
    path("time/", include('grade5.time.timeurls')),
    path("fractions/", include('grade5.fractions.grade5fractionsurls')),
    path("decimals/", include('grade5.decimals.grade5decimalsurls')),
    path("geometry/", include('grade5.geometry.grade5geometryurls'))
]
