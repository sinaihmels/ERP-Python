from django.contrib import admin
from .models import ProductClass, Item, Color

# Register your models here.
admin.site.register(ProductClass)
admin.site.register(Item)
admin.site.register(Color)