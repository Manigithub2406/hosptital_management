# registrations/models.py

from django.db import models

class Registration(models.Model):
    HOSPITAL_CATEGORIES = [
        ('GM', 'General Medicine'),
        ('OR', 'Orthopedics'),
        ('SU', 'Surgery'),
        ('PE', 'Pediatrics'),
        ('GY', 'Gynecology'),
        ('NE', 'Neurology'),
        ('ON', 'Oncology'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=30)  # Default value added
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    description = models.TextField(default='No description provided')  # Default value added
    category = models.CharField(max_length=2, choices=HOSPITAL_CATEGORIES, default='GM')  # Default value added

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
