# registrations/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Registration
from .forms import RegistrationForm

def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registrations/registration_list.html', {'registrations': registrations})

def registration_detail(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    return render(request, 'registrations/registration_detail.html', {'object': registration})

def registration_create(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'registrations/registration_form.html', {'form': form})

def registration_update(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    form = RegistrationForm(request.POST or None, instance=registration)
    if form.is_valid():
        form.save()
        return redirect('registration_detail', pk=registration.pk)
    return render(request, 'registrations/registration_form.html', {'form': form})

def registration_delete(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == "POST":
        registration.delete()
        return redirect('registration_list')
    return render(request, 'registrations/registration_confirm_delete.html', {'registration': registration})

def registration_success(request):  
    return render(request, 'registrations/success.html')
