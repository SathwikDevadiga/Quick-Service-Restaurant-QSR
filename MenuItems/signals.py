from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import MenuItem
from django.core.cache import cache

@receiver(post_save, sender=MenuItem)
def invalidate_menu_cache(sender, instance, **kwargs):
    """
    Invalidate the cache for the menu list when a MenuItem is created or updated.
    """
    cache.delete('menu_list')