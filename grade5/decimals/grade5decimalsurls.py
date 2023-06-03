from django.urls import path
from django.urls import path, include
from . import grade5decimalsviews

# URLConf
urlpatterns = [
    path('home/', grade5decimalsviews.grade5_decimals_home),
    path('compare/', include('grade5.decimals.compare.compare_decimals_urls')),
    path('round/', include('grade5.decimals.round.round_decimals_urls')),
    path('addition/', include('grade5.decimals.addition.addition_decimals_urls')),
    path('subtract/', include('grade5.decimals.subtract.subtract_decimals_urls')),
    path('multiply/', include('grade5.decimals.multiply.multiply_decimals_urls')),
    path('divide/', include('grade5.decimals.divide.divide_decimals_urls'))
]
