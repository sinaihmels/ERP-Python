from django.shortcuts import render
from .models import Order, Customer, Status, OrderItem
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def customers(response):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    return render(response, "customers/customers.html", {"orders": orders, "customers": customers})

def new_order(response):    
    customers = Customer.objects.all()
    return render(response, "customers/new_order.html", {"customers": customers})

def get_customer_info(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer': customer,}
    customer_info_html = render_to_string('customers/new_order.html', context)
    return HttpResponse(customer_info_html)
    