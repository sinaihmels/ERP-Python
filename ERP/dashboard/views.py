from django.shortcuts import render, HttpResponse, redirect
from .models import ProductClass, Item, Color
from .forms import CreateItemForm
from django.template.loader import render_to_string 
from django.utils.datastructures import MultiValueDictKeyError
from django.http import JsonResponse

# Create your views here.
def inventory(request):
    if request.method == "GET":
        items = Item.objects.all()
        classes = ProductClass.objects.all()
        color_choices = Color.objects.all()
        return render(request, "dashboard/inventory.html", {"items": items, "classes": classes, "color_choices": color_choices})
    
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
            return redirect("dashboard:inventory")


        if "edit_product" in request.POST:
            # an item was edited and the data about it was updated 
            # verify input
            form_data = request.POST
            item_id = form_data.get("edit_item_id")
            new_name = form_data.get("name").strip()
            new_description = form_data.get("description").strip()
            new_class_id = form_data.get("class")
            new_class = ProductClass.objects.get(pk=int(new_class_id))
            new_color = form_data.get("color")
            new_price  = form_data.get("price").strip()
            new_amount_instock = form_data.get("amount_instock")
            

            if not new_description or not new_amount_instock or int(new_amount_instock) <= 0 or not new_class or not new_color or not item_id:
                return HttpResponse("Please provide valid data", status=400)
            
            old_item = Item.objects.get(pk=item_id)
            try:
                new_image = request.FILES["image"]
                old_item.image = new_image
            except MultiValueDictKeyError as e:
                pass
            old_item.name = new_name
            old_item.description = new_description
            old_item.productclass = new_class
            old_item.color = new_color
            old_item.price = new_price
            old_item.amount_instock = new_amount_instock

            old_item.save()
            return redirect("dashboard:inventory")
        

    
        elif "delete_product" in request.POST:
            # a delete button for an item was pressed
            item_id = request.POST.get("delete_product")
            try: 
                item_to_delete = Item.objects.get(pk=item_id)
                item_to_delete.delete()
                return redirect("dashboard:inventory")
            except Item.DoesNotExist:
                return HttpResponse("Item not found", status=400)




def dashboard(request):

    return render(request, "dashboard/dashboard.html", {})



def stats_view(request):
    return render(request, "dashboard/stats.html")

def create_item_view(request):
    if request.method == "POST": 
        form = CreateItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dashboard:inventory")
    else:
        form = CreateItemForm()
    return render(request, "dashboard/create_item.html", {"form": form})


def get_edit_drawer(request, item_id):
    # You can implement logic here to fetch data related to the item if needed
    item_to_be_edited = Item.objects.get(pk=item_id)
    classes = ProductClass.objects.all()
    item_class_id = ProductClass.objects.get(name=item_to_be_edited.productclass)
    color_choices = Color.objects.all()
    context = {'item_to_be_edited': item_to_be_edited,"classes": classes, "item_class_id": item_class_id,"color_choices": color_choices}
    edit_drawer_content = render_to_string('dashboard/edit_drawer.html', context)
    return HttpResponse(edit_drawer_content)
