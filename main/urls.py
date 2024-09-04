# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('login/',views.login,name='login'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    
    ]
