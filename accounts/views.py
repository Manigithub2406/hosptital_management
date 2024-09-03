# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import DoctorRegistrationForm, ReceptionistRegistrationForm
from registrations.models import Registration
from django.contrib import messages


def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_login')
    else:
        form = DoctorRegistrationForm()
    return render(request, 'accounts/register_doctor.html', {'form': form})

def register_receptionist(request):
    if request.method == 'POST':
        form = ReceptionistRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receptionist_login')
    else:
        form = ReceptionistRegistrationForm()
    return render(request, 'accounts/register_receptionist.html', {'form': form})

# accounts/views.py

from .forms import DoctorLoginForm, ReceptionistLoginForm

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_doctor:
                login(request, user)
                return redirect('select_category') 
    else:
        form = DoctorLoginForm()
    return render(request, 'accounts/login_doctor.html', {'form': form})

def receptionist_login(request):
    if request.method == 'POST':
        form = ReceptionistLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_receptionist:
                login(request, user)
                return redirect('reception_view')
    else:
        form = ReceptionistLoginForm()
    return render(request, 'accounts/login_receptionist.html', {'form': form})

def reception_view(request):
    return render(request, 'accounts/reception_view.html')

def doctor_view(request, category):
    if not request.user.is_authenticated or not request.user.is_doctor:
        return redirect('doctor_login')
    
    registrations = Registration.objects.filter(category=category)
    return render(request, 'accounts/doctor_view.html', {'registrations': registrations})

def select_category(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        return redirect('doctor_view', category=category)
    return render(request, 'accounts/select_category.html')

