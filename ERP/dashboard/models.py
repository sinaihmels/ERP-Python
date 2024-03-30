from django.db import models

# Create your models here.
class ProductClass(models.Model):
    id = models.BigIntegerField().primary_key=True
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Item(models.Model):
    productclass = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    description = models.CharField(max_length=400)
    id = models.BigIntegerField().primary_key=True
    instock = models.BooleanField()
    amount_instock = models.PositiveBigIntegerField(default=1)
    color_choices = [ # These are tuples for the color choices possible 
        ('BL', 'Blue'),
        ('GN', 'Green'),
        ('GY', 'Grey'),
        ('PI', 'Pink'),
        ('RE', 'Red'),
        ('BE', 'Beige'),
        ('MC', 'Multicolor'),
        ('WH', 'White'),
        ('BA', 'Black'), 
        ('BR', 'Brown'), 
        ('SL', 'Silver'), 
        ('GO', 'Gold'),
        ('PU', 'Purple'),
    ]
    color = models.CharField(
        max_length= 100, 
        choices=color_choices,
        default='Multicolor')
    

    def __str__(self):
        return self.description