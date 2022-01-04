from django.contrib import admin
from django.db.models import fields

from .models import Brand, Country, Manufacturer, Unit, Category
from .models import Product

class AdminProduct(admin.ModelAdmin):

    list_display = ('name', 'art', 'country', 'manufacturer', 'unit', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'art',)
    list_filter = ('brand', 'country', 'manufacturer', 'unit', 'category',)
    fields = ('code', 'name', 'art', 'country', 'manufacturer', 'unit', 'category', 'descriptions',)
    class Meta:
        model = Product
    

# Register your models here.
admin.site.register(Brand)
admin.site.register(Country)
admin.site.register(Manufacturer)
admin.site.register(Unit)
admin.site.register(Category)

admin.site.register(Product, AdminProduct)

