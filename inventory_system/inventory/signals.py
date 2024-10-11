from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import InventoryItem, InventoryItemLog

@receiver(post_save, sender=InventoryItem)
def log_inventory_item_add_change(sender, instance, created, **kwargs):
    action = 'ADD' if created else 'CHANGE'
    InventoryItemLog.objects.create(
        action=action,
        item=instance,
        user=instance.user  # Assuming the instance has a user attribute
    )

@receiver(post_delete, sender=InventoryItem)
def log_inventory_item_delete(sender, instance, **kwargs):
    InventoryItemLog.objects.create(
        action='DELETE',
        item=instance
    )
