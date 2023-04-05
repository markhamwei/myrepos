from django.urls import path
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.addition_page)
]
