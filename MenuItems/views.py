from rest_framework import generics, permissions, status 
from rest_framework.permissions import BasePermission, IsAdminUser , SAFE_METHODS
from rest_framework.response import Response
from .models import MenuItem
from .serializer import MenuItemSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Custom permission: Allow only admins to modify, but all authenticated users can view
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# GET (cached for 15 mins), POST (admin only)
class MenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser | ReadOnly]

    @method_decorator(cache_page(60 * 15, key_prefix='menu_list'))
    def list(self, request, *args, **kwargs):
        """List all menu items with caching (15 min)"""
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        import time
        time.sleep(1)  # Simulate latency (for testing)
        return super().get_queryset()

# GET, PUT, DELETE (only admin can update/delete, others can only view)
class MenuItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

# GET only available menu items (visible to all authenticated users)
class AvailableMenuItemsView(generics.ListAPIView):
    queryset = MenuItem.objects.filter(availability=True)
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.IsAuthenticated]
