from django.urls import path
from django.urls import path
from . import grade5_equations_calculate_views

# URLConf
urlpatterns = [
    path('', grade5_equations_calculate_views.grade5_equations_calculate_page)
]
