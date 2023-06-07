from django.urls import path
from django.urls import path
from . import identify_triangles_views

# URLConf
urlpatterns = [
    path('', identify_triangles_views.triangles_identify_page)
]
