from django.shortcuts import render, HttpResponse, redirect
from .models import ProductClass, Item
from .forms import CreateItemForm

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
    
    elif request.method == "POST": 
        if "add_new_product" in request.POST:
            # a new item was added to the inventory
            # do I need to verify the input as the fields are all required on the front end
            form_data = request.POST
            new_name = form_data.get("name").strip()
            new_description = form_data.get("description").strip()
            new_class_id = form_data.get("class")
            new_class = ProductClass.objects.get(pk=int(new_class_id))
            new_color = form_data.get("color")
            new_price  = form_data.get("price").strip()
            amount_to_stock = form_data.get("amount_instock")
            new_image = request.FILES["image"]

            if not new_description or not amount_to_stock or int(amount_to_stock) <= 0 or not new_class or not new_color:
                return HttpResponse("Please provide valid data", status=400)
            
            # add the new item to the database
            new_item = Item(name=new_name, description=new_description, productclass=new_class, color=new_color, price=new_price, amount_instock=amount_to_stock,  image=new_image)
            # save the new_item to the database
            new_item.save()
            return redirect("dashboard:dashboard")


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
                return redirect("dashbard:dashboard")

                
            



def dashboard(response):
    return render(response, "dashboard/dashboard.html", {})

def create_item_view(request):
    if request.method == "POST": 
        form = CreateItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
    else:
        form = CreateItemForm()
    return render(request, "dashboard/create_item.html", {"form": form})