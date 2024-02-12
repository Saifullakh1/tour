from django.urls import path
from .views import list_guide

urlpatterns = [
    path('guides/', list_guide, name='list-guides')
]