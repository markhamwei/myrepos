from django.urls import path
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', additionviews.addition_page)
]
