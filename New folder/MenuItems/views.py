from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status , generics , permissions
from .models import MenuItem
from .serializer import MenuItemSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(60 * 15,key_prefix='menu_list'))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        """
        List all menu items with caching.
        """
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        import time
        time.sleep(1)  # Simulate a delay for testing purposes
        return super().get_queryset()
    
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]

class AvailableMenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(availability=True)
    serializer_class = MenuItemSerializer

    