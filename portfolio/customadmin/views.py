from django.shortcuts import render, redirect
from .models import Admin, Store
from django.shortcuts import get_object_or_404
from .forms import AdminForm

# Create your views here.

def admin_home(request):
    admins = Admin.objects.all()

    return render(request, 'customadmin/index.html', {'admins': admins})

def admin_detail(request, id):
    admin = get_object_or_404(Admin, id=id)
    return render(request, 'customadmin/detail.html', {'admin': admin})

def store(request):
    stores = None
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = AdminForm()
    return render(request, 'customadmin/store.html', {'stores': stores, 'form': form})