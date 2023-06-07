from django.urls import path
from django.urls import path, include
from . import grade5geometryviews

# URLConf
urlpatterns = [
    path('home/', grade5geometryviews.grade5_geometry_home),
    path('identifyangles/', include('grade5.geometry.identifyangles.identify_angles_urls')),
    path('identifytriangles/', include('grade5.geometry.identifytriangles.identify_triangles_urls')),
    #path('addition/', include('grade5.decimals.addition.addition_decimals_urls')),
    #path('subtract/', include('grade5.decimals.subtract.subtract_decimals_urls')),
    #path('multiply/', include('grade5.decimals.multiply.multiply_decimals_urls')),
    #path('divide/', include('grade5.decimals.divide.divide_decimals_urls'))
]
