# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),             # Public home page
    path('register/', views.register_view, name='register'),  # Registration page
    path('login/', views.login_view, name='login'),     # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Dashboard page
]
