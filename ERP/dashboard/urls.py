from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('inventory/', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
]