from django.shortcuts import render, redirect
from .models import Order, Customer, Status, OrderItem
from dashboard.models import Item, ProductClass, Color
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def customers(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    return render(request, "customers/customers.html", {"orders": orders, "customers": customers})

def new_order(request):    
    if request.method == "GET":
        customers = Customer.objects.all()
        items = Item.objects.all()
        classes = ProductClass.objects.all()
        color_choices = Color.objects.all()
        return render(request, "customers/new_order.html", {"customers": customers, "items": items, "classes": classes, "color_choices": color_choices})
    if request.method == "POST":
        form_data = request.POST
        customer_id = form_data.get("customers_in_database")
        # if there is no different delivery address given then the address in the database will be used 
        if not form_data.get("delivery_address"):
            address = Customer.objects.filter(pk=customer_id)
        else:
            address = form_data.get("delivery_address")
        # create a dictionary of the ordered products 
        list_item_ids = form_data.getlist("item_row_checkbox")  # Use getlist() to retrieve all selected values
        list_amounts_of_products = form_data.getlist("amount")
        item_id_amount = {}
        for i in range(len(list_item_ids)):
            item_id_amount[list_item_ids[i]]= list_amounts_of_products[i]
        new_order = Order(customer_id=customer_id, delivery_adress=address)
        new_order.save()
        order = Order.objects.filter(customer_id=customer_id, delivery_address=address)
        order_id = order.id
        # create OrderItems


        
        return redirect("customers:customers")


def get_customer_info(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer': customer}
    customer_info_html = render_to_string('customers/customer_info.html', context)
    return JsonResponse({'customer_info_html': customer_info_html})
    