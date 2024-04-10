
from django.db import models
from dashboard.models import Item
from customers.models import Customer

class Status(models.Model):
    id = models.BigIntegerField().primary_key=True
    name_of_status = models.CharField(max_length=100)

    def __str__(self):
        return self.name_of_status


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_address = models.CharField(max_length=400)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    id = models.BigIntegerField().primary_key=True
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()
