from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.grade6_home),
    path('variables/', include('grade6.variables.variablesurls'))
]