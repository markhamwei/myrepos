from django.urls import path
from django.urls import path
from . import identify_quadrilateral_views

# URLConf
urlpatterns = [
    path('', identify_quadrilateral_views.quadrilateral_identify_page)
]
