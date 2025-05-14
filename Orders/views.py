from django.shortcuts import render 

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics , permissions
from .models import Order
from OrderItems.models import OrderItem
from django.utils.timezone import now, timedelta

from .serializer import  OrderItemSerializer , OrderSerializer ,OrderCreateSerializer

class OrderDetail(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related('order_items__menu_item').all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['status']
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return super().get_serializer_class()
    

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class AverageDailySalesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        data = {}
        today = now().date()

        for i in range(1, 15): 
            day = today - timedelta(days=i)
            if day.weekday() < 5:  # Monday to Friday
                orders = Order.objects.filter(status='completed', timestamp__date=day)
                order_items = OrderItem.objects.filter(order__in=orders)

                total = sum(
                    item.menu_item.price * item.quantity
                    for item in order_items
                )
                data[str(day)] = total
                if len(data) == 4:
                    break

        return Response(data)
