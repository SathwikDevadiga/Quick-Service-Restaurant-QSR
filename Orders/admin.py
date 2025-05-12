from django.contrib import admin
from .models import Order
from OrderItems.models import OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ['menu_item', 'quantity']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'status']
    list_filter = ['status', 'timestamp']
    list_editable = ['status']
    inlines = [OrderItemInline]
