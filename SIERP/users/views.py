from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm

# Create your views here.

def users(request):
    return HttpResponse("This will be the login, logout, register forms")

def login(response):
    return render(response, "users/login.html")

def logout(response):
    return render(response, "users/logout.html")

def register(response):
    form = RegisterForm() # We initialize the form outside the if block
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect()

    
    if response.method == "GET":
        return render(response, "users/register.html", {"form": form})