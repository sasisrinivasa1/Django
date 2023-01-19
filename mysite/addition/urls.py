from django.urls import path
from . import views
urlpatterns = [
    path('plus/', views.plus),
    path('plus/add/', views.add),
]