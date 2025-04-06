from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('<int:id>/', views.admin_detail, name='admin_detail'),
]