from django.urls import path
from . import homeviews

# URLConf
urlpatterns =[
	path('home/', homeviews.my_page)
]