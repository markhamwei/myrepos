from django.urls import path
from django.urls import path, include
from . import grade5views

# URLConf
urlpatterns = [
    path('home/', grade5views.grade5_home),
    path("addition/", include('grade5.addition.additionurls')),
    path("subtract/", include('grade5.subtract.subtracturls')),
    path("multiply/", include('grade5.multiply.multiplyurls')),
    path("divide/", include('grade5.divide.divideurls')),
    path("length/", include('grade5.length.lengthurls')),
    path("time/", include('grade5.time.timeurls')),
	path("perimeterarea/", include('grade5.perimeterarea.perimeterareaurls')),
    path("fractions/", include('grade5.fractions.grade5fractionsurls'))
]
