# accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('receptionist/login/', views.receptionist_login, name='receptionist_login'),
    path('doctor/register/', views.register_doctor, name='doctor_register'),  # Adjust as needed
    path('receptionist/register/', views.register_receptionist, name='receptionist_register'),
    path('reception/', views.reception_view, name='recepetion_view'),
    path('select-category/', views.select_category, name='select_category'),
    path('doctor-view/<str:category>/', views.doctor_view, name='doctor_view'),
    ]
