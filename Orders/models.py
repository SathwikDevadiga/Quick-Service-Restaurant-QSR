from django.db import models
from MenuItems.models import MenuItem
import uuid as uuid_lib
from authentication.models import CustomUser


    

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=None)
    id = models.UUIDField(primary_key=True, default=uuid_lib.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    items = models.ManyToManyField(MenuItem, through='OrderItems.OrderItem', related_name='orders')

    def __str__(self):
        return f"Order #{self.id} - {self.status}"
    
    def get_total(self):
        return sum(item.item_subtotal for item in self.order_items.all())
