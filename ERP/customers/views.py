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
        customer_object = Customer.objects.get(pk=customer_id)
        # if there is no different delivery address given then the address in the database will be used 
        if not form_data.get("delivery_address"):
            address_database = Customer.objects.get(pk=customer_id)
            address = address_database.address
        else:
            address = form_data.get("delivery_address")
        # create a dictionary of the ordered products 
        list_item_ids = form_data.getlist("item_row_checkbox")  # Use getlist() to retrieve all selected values
        list_amounts_of_products = form_data.getlist("amount")
        # get the status object 
        status_object=Status.objects.get(pk=1)
                #item_id_amount = {}
        #for i in range(len(list_item_ids)):
            #item_id_amount[list_item_ids[i]]= list_amounts_of_products[i]
        new_order = Order(customer=customer_object, delivery_address=address, status=status_object)
        new_order.save()
        # create OrderItems
        for i in range(len(list_item_ids)):
            item_to_add = Item.objects.get(pk=list_item_ids[i])
            new_order_item = OrderItem(order=new_order, item=item_to_add, amount=list_amounts_of_products[i])
            new_order_item.save()
        return redirect("customers:customers")


def get_customer_info(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer': customer}
    customer_info_html = render_to_string('customers/customer_info.html', context)
    return JsonResponse({'customer_info_html': customer_info_html})
    
def get_details_drawer(request, order_id):
    order_to_be_detailed = Order.objects.get(pk=order_id)
    order_items = OrderItem.objects.filter(order=order_to_be_detailed)
    items = Item.objects.all()
    context = {"order_to_be_detailed": order_to_be_detailed, "order_items": order_items, "items": items}
    details_drawer_content = render_to_string('customers/details_drawer.html', context)
    return HttpResponse(details_drawer_content)