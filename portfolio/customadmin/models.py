from django.db import models
from django.utils import timezone

# Create your models here.

class Admin(models.Model):
    TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='admin_images/')
    date_added = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField(max_length=1000, default='')
    def __str__(self):
        return self.name
