from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('activate/<uid>/<token>', views.ActivateAccountView.as_views(), name='activate'),
]