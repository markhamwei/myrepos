from django.urls import path
from . import views

# URLConf
urlpatterns =[
	path('hello/', views.say_hello),
	path('query/', views.my_query),
	path('calculate/', views.calculate)
]