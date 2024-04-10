from django.db import models

class Customer(models.Model):
    id = models.BigIntegerField().primary_key=True
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=400)
    phone = models.BigIntegerField()

    def __str__(self):
        return self.name

