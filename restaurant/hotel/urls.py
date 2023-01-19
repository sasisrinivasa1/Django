from django.urls import path
from . import views

urlpatterns = [
    path('hotel/', views.hotel, name='hotel'),
    path('hotel/accounts/register', views.register, name='register'),
    path('hotel/accounts/login', views.login, name='login'),
    path('hotel/accounts/logout', views.logout, name='logout'),
]