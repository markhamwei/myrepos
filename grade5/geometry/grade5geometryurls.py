from django.urls import path
from django.urls import path, include
from . import grade5geometryviews

# URLConf
urlpatterns = [
    path('home/', grade5geometryviews.grade5_geometry_home),
    path('identifyangles/', include('grade5.geometry.identifyangles.identify_angles_urls')),
    path('identifytriangles/', include('grade5.geometry.identifytriangles.identify_triangles_urls')),
    path('identifyquadrilateral/', include('grade5.geometry.identifyquadrilateral.identify_quadrilateral_urls')),
    path('perimeterarea/', include('grade5.geometry.perimeterarea.perimeterareaurls')),
    path('volume/', include('grade5.geometry.volume.volumeurls')),
    #path('divide/', include('grade5.decimals.divide.divide_decimals_urls'))
]
