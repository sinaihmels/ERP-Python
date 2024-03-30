from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
]