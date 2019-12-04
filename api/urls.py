from django.urls import path
from .views import get_listings, ListDetailView, comments

urlpatterns = [
    path('listings/', get_listings),
    path('listings/<int:pk>/', ListDetailView.as_view()),
    path('listings/<int:pk>/comments/', comments),
]
