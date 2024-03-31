from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('inventory/', views.index, name='index'),
    path('', views.dashboard, name='dashboard'),
    path('create_item/', views.create_item_view, name='create_item'),
]