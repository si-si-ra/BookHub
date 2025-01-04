from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Role choices
    LIBRARIAN = 'librarian'
    PATRON = 'patron'
    ROLE_CHOICES = [
        (LIBRARIAN, 'Librarian'),
        (PATRON, 'Patron'),
    ]
    
    # Additional fields
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Meta data
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username} ({self.role})"




