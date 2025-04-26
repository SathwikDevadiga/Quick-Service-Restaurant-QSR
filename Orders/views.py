from django.shortcuts import render 

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Order
from django.utils.timezone import now, timedelta

from .serializer import  OrderItemSerializer , OrderSerializer ,OrderCreateSerializer

class OrderDetail(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    filterset_fields = ['status']
    
    

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateSerializer
        return super().get_serializer_class()
    

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class AverageDailySalesView(APIView):
    def get(self, request):
        data = {}
        today = now().date()

        for i in range(1, 15):  # look back up to 2 weeks to find 4 weekdays
            day = today - timedelta(days=i)
            if day.weekday() < 5:  # Monday to Friday
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
