from django.db import models

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    Item_Model = models.CharField(max_length=100, default="N/a")
    Serial_Number = models.CharField(max_length=100, default="N/a")
    quantity = models.PositiveIntegerField(default=1)
    #price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def __str__(self):
        return f"{self.name} - Model: {self.Item_Model}, S/N: {self.Serial_Number}"

class InventoryLog(models.Model):
    item = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    item_model = models.CharField(max_length=255, null=True, blank=True)  # Add item model
    serial_number = models.CharField(max_length=255, null=True, blank=True)  # Add serial number

    def __str__(self):
        return f"{self.item} - {self.action} - {self.item_model} - {self.serial_number} at {self.timestamp}"

class Map(models.Model):
    name = models.CharField(max_length=100)
    width = models.PositiveIntegerField(default=800)  # Width of the map
    height = models.PositiveIntegerField(default=600)  # Height of the map

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=100)
    map = models.ForeignKey(Map, on_delete=models.CASCADE)
    equipment = models.ManyToManyField(InventoryItem, blank=True)
    x_coordinate = models.PositiveIntegerField(default=0)  # Default X position
    y_coordinate = models.PositiveIntegerField(default=0)  # Default Y position

    def __str__(self):
        return self.name



