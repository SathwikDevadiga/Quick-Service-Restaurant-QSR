from django.apps import AppConfig


from django.dispatch import Signal

# Define a custom signal
order_created = Signal()

# orders/apps.py


