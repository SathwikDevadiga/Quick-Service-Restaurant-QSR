from rest_framework import serializers
from .models import OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='menu_item.name', read_only=True)
    item_price = serializers.DecimalField(source='menu_item.price', read_only=True, max_digits=10, decimal_places=2)
    #item_subtotal = serializers.DecimalField(source='item_subtotal', read_only=True, max_digits=10, decimal_places=2)
    class Meta:
        model = OrderItem
        fields = ('item_name','item_price', 'quantity')