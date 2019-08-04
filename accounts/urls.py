from django.urls import path
from . import views


urlpatterns = [
    path('dashbord', views.dashbord, name='dashbord'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')

]