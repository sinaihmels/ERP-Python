from django import template
from dashboard.models import ProductClass, Item

register = template.Library()

@register.inclusion_tag('dashboard/edit_drawer.html')
def edit_drawer(item_id):
    item_to_be_edited = Item.objects.get(pk=item_id)
    classes = ProductClass.objects.all()
    return {'item_to_be_edited': item_to_be_edited,"classes": classes, 
            "color_choices": [ 
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
            }