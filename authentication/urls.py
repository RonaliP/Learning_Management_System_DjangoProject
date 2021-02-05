from django.contrib import admin
from django.urls import path
from authentication.views import UserCreationAPIView, Login,Logout, ForgotPassword, ResetPassword, NewPassword

urlpatterns = [
    path('create-user/', UserCreationAPIView.as_view(), name='create-user'),
    path('login/', Login.as_view(), name='login'),
    path('forgot-password/', ForgotPassword.as_view(), name='forgot-password'),
    path('reset-password/', ResetPassword.as_view(), name='reset-password'),
    path('new-password/', NewPassword.as_view(), name='new-password'),
    path('logout/', Logout.as_view(), name='logout'),
]