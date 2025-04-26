
from django.db import models
from Orders.models import Order
from MenuItems.models import MenuItem
# Create your models here.


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='menu_item')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity}) in {self.order}"

    @property
    def item_subtotal(self):
        return self.menu_item.price * self.quantity
    

    class Meta:
        unique_together = ('order', 'menu_item')
