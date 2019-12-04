from django.urls import path
from .views import get_listings

urlpatterns = [
    path('listings/', get_listings),
]
