from django.urls import path
from . import views


app_name = "orders"
urlpatterns = [
    path("orders", views.orders, name="orders"),
    path("new_order", views.new_order, name="new_order"),
    path("get_customer_info/<int:customer_id>/", views.get_customer_info, name="get_customer_info"),
    path("get_details_drawer/<int:order_id>/", views.get_details_drawer, name="get_details_drawer"),
]