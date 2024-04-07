from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    path("", views.customers, name="customers"),
    path("new_order", views.new_order, name="new_order"),
    path('get_customer_info/<int:customer_id>/', views.get_customer_info, name='get_customer_info'),
]