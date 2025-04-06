from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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



    # One to Many relationship
class Admin_review(models.Model):
    name = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000, default='')
    date_added = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.user.username} review for {self.name.name}"


# many to many relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    users = models.ManyToManyField(Admin, related_name='stores')
    def __str__(self):
        return self.name
    
# class Certificate(models.Model):
#     name = models.OneToOneField(Admin, on_delete=models.CASCADE, related_name='certificates')
#     certificate_number = models.CharField(max_length=100)
#     date_added = models.DateTimeField(default=timezone.now)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     def __str__(self):
#         return f'certificate for {self.name.name}'






