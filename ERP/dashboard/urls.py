from django.urls import path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('', views.dashboard, name='dashboard'),
    path('get_edit_drawer/<int:item_id>/', views.get_edit_drawer, name='get_edit_drawer'),
    path('create_item/', views.create_item_view, name='create_item'),
    path('datenschutz/', views.datenschutz_view, name='datenschutz'),
    path('impressum/', views.impressum_view, name='impressum'),
    path('nutzungsbedingungen/', views.nutzungsbedingungen_view, name='nutzungsbedingungen'),

]