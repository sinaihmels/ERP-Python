from django.db import models
from dashboard.models import Item

class Customer(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=400)
    phone = models.BigIntegerField()


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    name_of_status = models.CharField(max_length=100)

class Order(models.Model):
    id = models.BigIntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    notes = models.TextField(max_length=400)
    delivery_address = models.CharField(max_length=400)
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default="unknown")

class OrderItem(models.Model):
    id = models.BigIntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField()
