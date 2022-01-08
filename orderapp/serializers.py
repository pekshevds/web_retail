from typing import ItemsView
from rest_framework import serializers
from .models import Order, ItemOrder

from customerapp.serializers import CustomerSerializer

class ItemOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemOrder
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    
    items = ItemOrderSerializer(many=True, read_only=True)
    customer = CustomerSerializer(many=False, read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'order_date', 'order_number', 'customer', 'total', 'items',)