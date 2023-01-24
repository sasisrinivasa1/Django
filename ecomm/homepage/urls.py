from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(), name='activate'),
    path('forgot-password/', views.resetpassword, name='resetpassword'),
    path('reset-password/<uidb64>/<token>/', views.ResetPasswordView.as_view(), name='reset-password'),
]