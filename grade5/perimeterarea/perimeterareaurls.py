from django.urls import path, include
from . import perimeterareaviews

# URLConf
urlpatterns = [
    path('', perimeterareaviews.perimeterarea_page),
    path('perimeter/',  include('grade5.perimeterarea.perimeter.perimeterurls')),
    path('area/', include('grade5.perimeterarea.area.areaurls')),
]
