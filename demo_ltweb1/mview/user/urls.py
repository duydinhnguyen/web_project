from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'user'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', auth_views.LogoutView.as_view(template_name='mv/home.html'), name='logout'),
    path('profile', views.profile, name='profile'),
]
