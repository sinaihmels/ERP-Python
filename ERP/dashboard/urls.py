from django.urls import path, re_path
from . import views

app_name = "dashboard"
urlpatterns = [
    path('inventory/', views.inventory, name='inventory'),
    path('', views.dashboard, name='dashboard'),
    path('get_edit_drawer/<int:item_id>/', views.get_edit_drawer, name='get_edit_drawer'),
    path('create_item/', views.create_item_view, name='create_item'),
    re_path(r'^get_pdf_items/(?P<item_ids>(\d+\/))+$', views.get_pdf_items, name='get_pdf_items'),
]