from django.shortcuts import render, redirect
from .models import Customer
from orders.models import Order, Status, OrderItem
from dashboard.models import Item, ProductClass, Color
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


# Create your views here.
def customers(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        return render(request, "customers/customers.html", {"customers": customers})
    elif request.method == "POST":
        if "details_customer" in request.POST:
            # the data of a customer was edited
            form_data = request.POST
            customer_object = Customer.objects.get(pk=form_data.get("details_customer_id"))
            customer_object.name = form_data.get("customer_name")
            customer_object.email = form_data.get("customer_email")
            customer_object.address = form_data.get("customer_address")
            customer_object.phone = form_data.get("customer_phone")
            customer_object.save()
            return redirect("customers:customers")

        elif "delete_customer" in request.POST:
            # a delete button for an item was pressed
            customer_id = request.POST.get("delete_customer")
            try: 
                customer_to_delete = Customer.objects.get(pk=customer_id)
                customer_to_delete.delete()
                return redirect("customers:customers")
            except Customer.DoesNotExist:
                return HttpResponse("Customer not found", status=400)

        
def new_customer(request):    
    if request.method == "GET":
        return render(request, "customers/new_customer.html/", {})
    
    if request.method == "POST":
        form_data = request.POST
        new_customer_name = form_data.get("new_customer_name")
        new_customer_email = form_data.get("new_customer_email")
        new_customer_address = form_data.get("new_customer_address")
        new_customer_phone = form_data.get("new_customer_phone")
        if not new_customer_address or not new_customer_email or not new_customer_name or not new_customer_phone: 
            return HttpResponse("Invalid input", status=400)
        Customer.objects.create(name=new_customer_name, email=new_customer_email, address=new_customer_address, phone=new_customer_phone)
        print("success")
        return redirect("customers:customers")


def get_customer_info(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    context = {'customer': customer}
    customer_info_html = render_to_string('customers/customer_info.html', context)
    return JsonResponse({'customer_info_html': customer_info_html})
    
def get_customer_details_drawer(request, customer_id):
    customer_to_be_detailed = Customer.objects.get(pk=customer_id)
    context = {"customer": customer_to_be_detailed}
    details_drawer_content = render_to_string('customers/customer_drawer.html', context)
    return HttpResponse(details_drawer_content)
