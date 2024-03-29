# urls.py
from django.urls import path
from users import views as v
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', v.register, name="register"),

]