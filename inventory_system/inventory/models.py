from django.db import models
from django.utils import timezone
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    Item_Model = models.CharField(max_length=100, default="N/a")
    Serial_Number = models.CharField(max_length=100, default="N/a")
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return f"{self.name} - Model: {self.Item_Model}, S/N: {self.Serial_Number}"

class InventoryLog(models.Model):
    item = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_model = models.CharField(max_length=255, null=True, blank=True)  # Add item model
    serial_number = models.CharField(max_length=255, null=True, blank=True)  # Add serial number
    class Meta:
            verbose_name_plural = "(ADMIN) Inventory Logs"
    def __str__(self):
        return f"{self.item} - {self.action} - {self.item_model} - {self.serial_number} at {self.timestamp}"


class Line(models.Model):
    startX = models.FloatField()
    startY = models.FloatField()
    endX = models.FloatField()
    endY = models.FloatField()
    color = models.CharField(max_length=7)  # Hex color for the line

    def __str__(self):
        return f"Line from ({self.startX}, {self.startY}) to ({self.endX}, {self.endY})"
class Station(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()  # Latitude field for geographic coordinate
    longitude = models.FloatField()  # Longitude field for geographic coordinate
    items = models.ManyToManyField(InventoryItem, blank=True)  # Many-to-Many relationship with InventoryItem

    def __str__(self):
        return self.name
    
class StationLog(models.Model):
    station = models.ForeignKey('Station', on_delete=models.CASCADE)  # Link to the Station model
    action = models.CharField(max_length=100)  # Action performed (e.g., "Added", "Updated", "Deleted")
    timestamp = models.DateTimeField(default=timezone.now)  # Time when the action was logged
    class Meta:
                verbose_name_plural = "(ADMIN) Station Logs"
    class Meta:
        ordering = ['-timestamp']  # Order logs by latest first
        verbose_name_plural = "Station Logs"

    def __str__(self):
        return f"{self.action} - {self.station.name} at {self.timestamp}"
    
    
class Map(models.Model):
    name = models.CharField(max_length=255)  # Name of the map
    width = models.IntegerField(default=800)  # Width of the map
    height = models.IntegerField(default=600)  # Height of the map

    def __str__(self):
        return self.name