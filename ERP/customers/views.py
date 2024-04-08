from django.shortcuts import render
from .models import Order, Customer, Status, OrderItem
from dashboard.models import Item
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

# Create your views here.
def customers(response):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    return render(response, "customers/customers.html", {"orders": orders, "customers": customers})

def new_order(response):    
    customers = Customer.objects.all()
    items = Item.objects.all()
    return render(response, "customers/new_order.html", {"customers": customers, "items": items})

def get_customer_info(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer': customer}
    customer_info_html = render_to_string('customers/customer_info.html', context)
    return JsonResponse({'customer_info_html': customer_info_html})
    