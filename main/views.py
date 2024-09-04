# main/views.py

from django.shortcuts import render, redirect



def home(request):
    return render(request, 'main/home.html')

def services(request):
    return render(request, 'main/services.html')

def login(request):
    return render(request, 'main/login.html')


def about(request):
    return render(request, 'main/about.html')

def book_appointment(request):
    return render(request, 'main/book_appointment.html')



