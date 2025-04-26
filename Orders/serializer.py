from rest_framework import serializers
from .models import Order
from OrderItems.models import OrderItem
from MenuItems.models import MenuItem
from OrderItems.serializer import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)  # ✅ match the related_name
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.order_items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields = ('id', 'timestamp', 'status', 'order_items','total_price',)



class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ('menu_item', 'quantity')
    order_items = OrderItemSerializer(many=True)

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        if not order_items_data:
            raise serializers.ValidationError("At least one order item is required.")
        
        unavailable_items = []
        for item_data in order_items_data:
            menu_item = item_data['menu_item']
            
            if not menu_item.availability:
                unavailable_items.append(menu_item.name)
        
        print(f"Unavailable items: {unavailable_items}")
        if unavailable_items:
            raise serializers.ValidationError({
                "unavailable_items": f"The following items are unavailable: {', '.join(unavailable_items)}"
            })
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            
            OrderItem.objects.create(order=order, **item_data)

        return order

    class Meta:
        model = Order
        fields = ('status', 'order_items')

    

    