from django.urls import path
from .views import get_listings, ListDetailView

urlpatterns = [
    path('listings/', get_listings),
    path('listings/<int:pk>/', ListDetailView.as_view()),
]
