from django.urls import path

from .views import CarsAPIView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('cars/', CarsAPIView.as_view()),

    
]
