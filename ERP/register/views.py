from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form":form})

@login_required(login_url="login/")
def logout_view(request):
    if request.method == "POST":
        auth_logout(request)    
        return HttpResponse("Successfully logged out", status=200)
    elif request.method == "GET":
        return render(request, "registration/logout.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to a success page or home page
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    