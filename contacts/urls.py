from django.urls import path
from . import views


url_patterns = [
    path('contact', views.contact, name='contact' ),
]