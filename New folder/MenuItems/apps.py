from django.apps import AppConfig


class MenuitemsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MenuItems'

    def ready(self):
        from . import signals
