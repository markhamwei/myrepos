from django.urls import path
from django.urls import path, include
from . import variablesviews

urlpatterns = [
    path('', variablesviews.variables_home),
    path('evaluating', include('grade6.variables.evaluating.evaluatingurls'))
]