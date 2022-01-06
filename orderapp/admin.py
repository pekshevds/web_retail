from django.contrib import admin
from .models import Order, ItemOrder
# Register your models here.


class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder
    fk_name = "order"

    fields = ('item_number', 'product', 'price', 'quant', 'total',)
    readonly_fields = ('item_number', 'product',)
    

class AdminOrder(admin.ModelAdmin):

    list_display = ('representation', 'order_date', 'order_number', 'customer', 'total',)
    list_display_links = ('representation',)
    
    fields = ('order_number', 'order_date', 'customer', 'total',)
    readonly_fields = ('order_date','order_number', 'total',)
    
    inlines = [ItemOrderInLine,]

    class Meta:
        model = Order
    

admin.site.register(Order, AdminOrder)