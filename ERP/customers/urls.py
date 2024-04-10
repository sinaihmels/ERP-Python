from django.urls import path
from . import views


app_name = "customers"
urlpatterns = [
    path("customers/", views.customers, name="customers"),
    path("customers/new_customer/", views.new_customer, name="new_customer"),
    path("get_customer_info/<int:customer_id>/", views.get_customer_info, name="get_customer_info"),
    path("get_customer_details_drawer/<int:customer_id>/", views.get_customer_details_drawer, name="get_customer_details_drawer"),
]