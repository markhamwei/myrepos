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
    path("geometry/", include('grade5.geometry.grade5geometryurls')),
    path("grids/", include('grade5.grids.grids_urls')),
    path("pattern/", include('grade5.pattern.pattern_urls')),
    path("equations/", include('grade5.equations.grade5equationsurls')),
    path("factoring/", include('grade5.factoring.grade5factoringurls')),
    path("probability/", include('grade5.probability.grade5_probability_urls'))
]
