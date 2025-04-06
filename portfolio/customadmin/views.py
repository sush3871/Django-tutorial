from django.shortcuts import render
from .models import Admin
from django.shortcuts import get_object_or_404
# Create your views here.

def admin_home(request):
    admins = Admin.objects.all()

    return render(request, 'customadmin/index.html', {'admins': admins})

def admin_detail(request, id):
    admin = get_object_or_404(Admin, id=id)
    return render(request, 'customadmin/detail.html', {'admin': admin})
