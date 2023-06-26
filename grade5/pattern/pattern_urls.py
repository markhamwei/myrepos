from django.urls import path
from django.urls import path
from . import pattern_views

# URLConf
urlpatterns = [
    path('', pattern_views.pattern_page)
]
