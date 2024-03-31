from django import forms
from .models import Item

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            "productclass", "description", "amount_instock", "color", "image"
        ]