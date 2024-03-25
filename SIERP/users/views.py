from django.shortcuts import render, HttpResponse

# Create your views here.


def users(request):
    return HttpResponse("This will be the login, logout, register forms")