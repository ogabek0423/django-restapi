from django.contrib import admin
from .models import Address, Apartment, City, Category, SellType

admin.site.register([Address, Apartment, City, Category, SellType])
