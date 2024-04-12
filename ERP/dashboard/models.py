from django.db import models

# Create your models here.
class ProductClass(models.Model):
    id = models.BigIntegerField().primary_key=True
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Color(models.Model):
    id = models.BigIntegerField().primary_key=True
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.color

class Item(models.Model):
    productclass = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    id = models.BigIntegerField().primary_key=True
    amount_instock = models.PositiveBigIntegerField(default=1)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="uploads/")
    price = models.FloatField(default=0)
    name = models.CharField(max_length=100, default="name") # TODO: Maybe remove default="name"????

    def __str__(self):
        return self.name
    
