from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , generics
from .models import MenuItem
from .serializer import MenuItemSerializer


class MenuItemDetail(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class AvailableMenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(availability=True)
    serializer_class = MenuItemSerializer

    