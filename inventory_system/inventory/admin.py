from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Map, Station, InventoryItem, InventoryLog  # Import your models
from django.utils.html import format_html, mark_safe

class InventoryItemAdmin(admin.ModelAdmin):
    search_fields = ['name', 'Item_Model', 'Serial_Number']
    list_display = ('name', 'Item_Model', 'Serial_Number')  # Define the fields to display
    list_display_links = ('name',)  # Make the name clickable to edit
    list_per_page = 10  # Set to display a maximum of 50 items

    # Method to display logs for each InventoryItem
    def display_logs(self, obj):
        # Fetch all logs for the item based on the name
        logs = InventoryLog.objects.filter(item=obj.name).order_by('-timestamp')  # Get logs in descending order
        
        if logs.exists():
            # Format logs into a simple HTML list, including the item name
            log_list = "<ul>"
            for log in logs:
                log_list += f"<li>{log.item} - at {log.timestamp}</li>"  # Display item name and action
            log_list += "</ul>"
            
            return mark_safe(log_list)  # Return the log list as safe HTML to display in admin
        return "No logs available"
    
    display_logs.short_description = 'Inventory Logs'
    
    def delete_selected(self, request, queryset):
        for obj in queryset:
            item_name = obj.name
            item_model = obj.Item_Model
            serial_number = obj.Serial_Number

            # Log the deletion with item name, model, and serial number
            InventoryLog.objects.create(
                item=item_name, 
                action="Deleted", 
                item_model=item_model, 
                serial_number=serial_number
            )
        queryset.delete()
    delete_selected.short_description = "Delete selected items and log"
    
    actions = ['delete_selected'] 
    
    def save_model(self, request, obj, form, change):
        quantity = obj.quantity
        for _ in range(quantity):
            new_item = InventoryItem(
                name=obj.name,
                Item_Model=obj.Item_Model,
                Serial_Number=obj.Serial_Number,
                quantity=1
            )
            new_item.save()

            # Log the creation with item name, model, and serial number
            InventoryLog.objects.create(
                item=new_item.name, 
                action="Added", 
                item_model=new_item.Item_Model, 
                serial_number=new_item.Serial_Number
            )
    def delete_model(self, request, obj):
        item_name = obj.name
        item_model = obj.Item_Model
        serial_number = obj.Serial_Number

        # Log the deletion with item name, model, and serial number
        InventoryLog.objects.create(
            item=item_name, 
            action="Deleted", 
            item_model=item_model, 
            serial_number=serial_number
        )
        obj.delete()
        
        
    class Media:
        css = {
            'all': ('inventory/css/custom_admin.css',)  # Link to your custom CSS file
        }

    def changelist_view(self, request, extra_context=None):
        # Fetch the latest 50 logs for display in the inventory item admin
        logs = InventoryLog.objects.all().order_by('-timestamp')[:50]
        extra_context = {'logs': logs}  # Add logs to the context
        return super().changelist_view(request, extra_context=extra_context)

class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'item_model', 'serial_number', 'action', 'timestamp')
class StationAdmin(admin.ModelAdmin):
    # Any existing code for the Station admin view
    pass

class MapAdmin(admin.ModelAdmin):
    change_list_template = "inventory/map_view.html"  # Your custom template

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/', self.admin_site.admin_view(self.map_view), name='map_view'),
        ]
        return custom_urls + urls

    def map_view(self, request, object_id):
        map_instance = get_object_or_404(Map, id=object_id)
        stations = Station.objects.filter(map=map_instance)
        return render(request, "inventory/map_view.html", {'map': map_instance, 'stations': stations})

# Register your models
admin.site.register(Station, StationAdmin)  # Register Station
admin.site.register(Map, MapAdmin)  # Register Map with the custom view
admin.site.register(InventoryItem, InventoryItemAdmin)  # Register InventoryItem with custom admin
admin.site.register(InventoryLog, InventoryLogAdmin)