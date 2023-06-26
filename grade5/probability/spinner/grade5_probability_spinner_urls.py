from django.urls import path
from django.urls import path
from . import grade5_probability_spinner_views

# URLConf
urlpatterns = [
    path('', grade5_probability_spinner_views.grade5_probability_spinner_page)
]
