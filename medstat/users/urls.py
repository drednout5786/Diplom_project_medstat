from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('success_register/', views.UserLoginView_2.as_view(), name='success_register')
]