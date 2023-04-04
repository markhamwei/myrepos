from django.urls import path
from django.urls import path, include
from . import views

# URLConf
urlpatterns = [
    path('home/', views.grade5_home),
    path("addition/", include('grade5.addition.myurls'))
]
