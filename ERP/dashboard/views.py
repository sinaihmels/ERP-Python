from django.shortcuts import render, HttpResponse
from .models import ProductClass, Item

# Create your views here.
def index(request):
    if request.method == "GET":
        items = Item.objects.all()
        classes = ProductClass.objects.all()
        return render(request, "dashboard/inventory.html", {"items": items, "classes": classes, "color_choices": [ 
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
        ]})
    if request.method == "POST": 
        if "update_inventory" in request.POST:
            # a new item was added to the inventory
            # verify input
            new_description = request.POST.get("description").strip()
            if not new_description:
                return HttpResponse("Please provide a description", status=400)
            amount_to_stock = request.POST.get("amount")
            if not amount_to_stock or int(amount_to_stock) <= 0:
                return HttpResponse("Please provide a valid amount of the product", status=400)
            new_color = request.POST.get("color")
            new_class_id = request.POST.get("class")
            new_class = ProductClass.objects.get(pk=int(new_class_id))
            if not new_class:
                return HttpResponse("Please provide a valid class", status=400)
            if not new_color:
                return HttpResponse("Please provide a valid color", status=400)
            # add the new item to the database
            new_item = Item(productclass=new_class, description=new_description, instock=True, amount_instock=amount_to_stock, color=new_color)
            # save the new_item to the database
            new_item.save()
            return HttpResponse("Successfully added!", status=200)

        elif "update_amount" in request.POST:
            # the amount of an item in the inventory was updated
            # verify input
            new_amount = request.POST.get("new_amount")

            if not new_amount or new_amount < 0:
                return HttpResponse("Please provide a valid amount", status=400)
            # update amount in the database
            else:
                id = request.POST.get("update_amount")
                item_to_change = Item.objects.get(pk=id)
                item_to_change.amount_instock = new_amount
                item_to_change.save()
                
            



def dashboard(response):
    return render(response, "dashboard/dashboard.html", {})