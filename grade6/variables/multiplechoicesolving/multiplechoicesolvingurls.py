from django.urls import path
from . import multiplechoicesolvingviews

urlpatterns = [
    path('', multiplechoicesolvingviews.page)
]