from django.urls import path
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html')),
    path('register/', views.register_page)
]