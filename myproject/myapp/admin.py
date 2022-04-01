#admin.py
from django.contrib import admin
from myapp.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Customer, CustomerAdmin)