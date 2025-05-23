from rest_framework import serializers
from .models import Order
from OrderItems.models import OrderItem
from MenuItems.models import MenuItem
from OrderItems.serializer import OrderItemSerializer
from .signals import order_created



class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)  
    total_price = serializers.SerializerMethodField(method_name='total')

    def total(self, obj):
        order_items = obj.order_items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields = ('id','user','timestamp', 'status', 'order_items','total_price')



class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ('menu_item', 'quantity', 'item_subtotal')
    order_items = OrderItemSerializer(many=True)

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        if not order_items_data:
            raise serializers.ValidationError("At least one order item is required.")
        
        user = self.context['request'].user

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
        order = Order.objects.create(user=user,**validated_data)
        for item_data in order_items_data:
            
            OrderItem.objects.create(order=order, **item_data)

        order_created.send(sender=Order, order=order)
        return order

    class Meta:
        model = Order
        fields = ('status', 'order_items')

    

    