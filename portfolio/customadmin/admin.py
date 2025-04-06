from django.contrib import admin
from .models import Admin, Store, Admin_review

# Register your models here.


# class AdminAdmin(admin.TabularInline):
#     model = Admin
#     extra = 2

# class StoreAdmin(admin.TabularInline):
#     list_display = ('name', 'date_added', 'type')




admin.site.register(Admin)
# admin.site.register(Store)
# admin.site.register(Certificate)
# admin.site.register(Admin_review)
