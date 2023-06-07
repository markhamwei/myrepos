from django.urls import path
from django.urls import path
from . import identify_angles_views

# URLConf
urlpatterns = [
    path('', identify_angles_views.angles_identify_page)
]
