from django.contrib import admin

from .models import Address, City, Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Address)
class Addressadmin(admin.ModelAdmin):
    pass
