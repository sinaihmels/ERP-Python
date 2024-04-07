from django.contrib import admin
from .models import Customer, Status, Order, OrderItem

# Register your models here.
admin.site.register(Customer)
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderItem)