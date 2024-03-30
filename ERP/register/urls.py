from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]