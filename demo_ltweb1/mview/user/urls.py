from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy

app_name = 'user'
urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mv/home.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', PasswordResetView.as_view(success_url=reverse_lazy('password-reset-done')), name='password-reset'),
    path('reset-password-done/', PasswordResetDoneView.as_view(),name='password-reset-done'),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),  name='password_reset_confirm' ),
    path('reset-password-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
