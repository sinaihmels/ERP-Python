from django.contrib import admin
from .models import Status, Order, OrderItem

# Register your models here.
admin.site.register(Status)
admin.site.register(Order)
admin.site.register(OrderItem)