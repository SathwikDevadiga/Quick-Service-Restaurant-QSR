from django.shortcuts import render 

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics , permissions
from .models import Order
from django.utils.timezone import now, timedelta

from .serializer import  OrderItemSerializer , OrderSerializer ,OrderCreateSerializer

class OrderDetail(generics.ListCreateAPIView):
    queryset = Order.objects.prefetch_related('order_items').all()
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
            if day.weekday() < 5: 
                orders = Order.objects.filter(status='completed', timestamp__date=day)
                total = sum(
                    item.menu_item.price * item.quantity
                    for order in orders
                    for item in order.items.all()
                )
                data[str(day)] = total
                if len(data) == 4:
                    break

        return Response(data)


'''
@api_view(['GET'])
def orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
'''
