from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Orders'
    def ready(self):
        from . import signals

# orders/apps.py


