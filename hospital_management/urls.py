# hospital_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('registrations/', include('registrations.urls')),
    path('accounts/', include('accounts.urls')),
]
