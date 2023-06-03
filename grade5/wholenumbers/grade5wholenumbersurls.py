from django.urls import path
from django.urls import path, include
from . import grade5wholenumbersviews

# URLConf
urlpatterns = [
    path('home/', grade5wholenumbersviews.grade5_wholenumbers_home),
    path('addition/', include('grade5.wholenumbers.addition.additionurls')),
    path('subtract/', include('grade5.wholenumbers.subtract.subtracturls')),
    path('multiply/', include('grade5.wholenumbers.multiply.multiplyurls')),
    path('divide/', include('grade5.wholenumbers.divide.divideurls'))
]
