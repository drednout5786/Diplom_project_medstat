from django.contrib import admin
from django.urls import path, include
from users import views
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('success_verification/', views.success_verification, name='success_verification'),
    path('subscribe/<int:pk>/', views.SubscribeUpdateView.as_view(), name='subscribe'),
    path('success_subscribe/', views.success_subscribe, name='success_subscribe'),
    path('get_api_token/', views.get_api_token, name='get_api_token'),
    path('update_api_token/', views.update_api_token, name='update_api_token'),
]