from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('delete_account/', views.delete_account, name='delete_account'),
    # reset password
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='accounts/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

]
