from django.contrib import admin

from .models import Customer


class AdminCustomer(admin.ModelAdmin):

    list_display = ('name', 'inn', 'kpp', )
    list_display_links = ('name',)
    search_fields = ('name', 'inn', )
    list_filter = ('kpp', )
    fields = ('user', 'name', 'inn', 'kpp', )
    class Meta:
        model = Customer
    

# Register your models here.

admin.site.register(Customer, AdminCustomer)

