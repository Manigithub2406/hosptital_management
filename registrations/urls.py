# registrations/urls.py

from django.urls import path
from .views import registration_list, registration_detail, registration_create, registration_update, registration_delete, registration_success

urlpatterns = [
    path('', registration_list, name='registration_list'),
    path('create/', registration_create, name='registration_create'),
    path('<int:pk>/', registration_detail, name='registration_detail'),
    path('<int:pk>/edit/', registration_update, name='registration_update'),
    path('<int:pk>/delete/', registration_delete, name='registration_delete'),
    path('success/', registration_success, name='registration_success'),  # Success URL
]
