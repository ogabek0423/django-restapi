from django.contrib import admin
from .models import Address, Apartment, City, Category, SellType
from import_export.admin import ImportExportModelAdmin

# admin.site.register([Address, Apartment, City, Category, SellType])


@admin.register(Apartment)
class ApartmentAdmin(ImportExportModelAdmin):
    list_display = ['category', 'short_name', 'address', 'phone', 'square', 'rooms']
    list_display_links = ['category', 'address', 'phone', 'square', 'rooms']
    search_fields = ['category', 'address', 'phone', 'square', 'rooms']


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ['name', 'city_id']
    list_display_links = ['name', 'city_id']
    search_fields = ['name', 'city_id']


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ['name', 'country']
    list_display_links = ['name', 'country']
    search_fields = ['name', 'country']


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'views']
    list_display_links = ['name', 'views']
    search_fields = ['name', 'views']


@admin.register(SellType)
class SellTypeAdmin(admin.ModelAdmin):
    list_display = ['nane']
    list_display_links = ['nane']
    search_fields = ['name']



