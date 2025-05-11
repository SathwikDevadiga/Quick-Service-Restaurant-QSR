from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , generics , permissions
from .models import MenuItem
from .serializer import MenuItemSerializer



class MenuItemDetail(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class AvailableMenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(availability=True)
    serializer_class = MenuItemSerializer

    