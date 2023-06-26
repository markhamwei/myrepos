from django.urls import path
from django.urls import path, include
from . import grade5equationsviews

# URLConf
urlpatterns = [
    path('home/', grade5equationsviews.grade5_equations_home),
    path('calculate/', include('grade5.equations.calculate.grade5_equations_calculate_urls')),
    #path('subtract/', include('grade5.wholenumbers.subtract.subtracturls')),
    #path('multiply/', include('grade5.wholenumbers.multiply.multiplyurls')),
    #path('divide/', include('grade5.wholenumbers.divide.divideurls'))
]
