from django.urls import path
from django.urls import path, include
from . import grade5views

# URLConf
urlpatterns = [
    path('home/', grade5views.grade5_home),
    path("addition/", include('grade5.addition.additionurls')),
    path("subtract/", include('grade5.subtract.subtracturls')),
    path("multiply/", include('grade5.multiply.multiplyurls')),
    path("divide/", include('grade5.divide.divideurls'))
]
