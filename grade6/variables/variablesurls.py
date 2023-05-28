from django.urls import path
from django.urls import path, include
from . import variablesviews

urlpatterns = [
    path('', variablesviews.variables_home),
    path('evaluating', include('grade6.variables.evaluating.evaluatingurls')),
    path('multiplechoicesolving', include('grade6.variables.multiplechoicesolving.multiplechoicesolvingurls')),
    path('basicsolving', include('grade6.variables.basicsolving.basicsolvingurls'))
]