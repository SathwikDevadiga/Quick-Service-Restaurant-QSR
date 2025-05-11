from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,generics ,permissions
from .models import OrderItem
from .serializer import OrderItemSerializer
# Create your views here.

class OrderItemsDetails(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

