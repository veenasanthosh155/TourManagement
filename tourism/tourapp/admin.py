from django.contrib import admin

# Register your models here.
from tourapp.models import Package,Booking
admin.site.register(Package)
admin.site.register(Booking)