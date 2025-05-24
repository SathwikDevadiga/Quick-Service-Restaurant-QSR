from django.core.mail import send_mail
from .models import Order
from django.dispatch import receiver

from django.dispatch import Signal

# Define a custom signal
order_created = Signal()

@receiver(order_created)
def send_order_confirmation_email(sender, order, **kwargs):
    items = order.order_items.all()
    item_lines = "\n".join(
        f"{item.menu_item.name} (x{item.quantity}) - ₹{item.item_subtotal}"
        for item in items
    ) 
    message = (
        f"Thank you for your order!\n\n"
        f"Order ID: {order.id}\n"
        f'timestamp: {order.timestamp}\n'
        f"Items:\n{item_lines or 'No items'}\n"
        f"Total: ₹{order.get_total()}\n\n"
        f"We will notify you once your order is ready."
    )

    recipient = order.user.email  # or order.customer.email if you have that
    send_mail(
        subject=f"Order #{order.id} Confirmation",
        message=message,
        from_email='your_email@example.com',
        recipient_list=[recipient],
        fail_silently=False,
    )
