from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tour/<int:id>/', views.tour_detail, name='tour-detail')
]