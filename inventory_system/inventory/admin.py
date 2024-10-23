from django.contrib import admin
from .forms import StationForm
from django.http import HttpResponseRedirect
from django.urls import path
from django.shortcuts import render
from .models import Station, Line, InventoryItem, InventoryLog, StationLog  # Import your models
from django.utils.html import format_html

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

        # Add the logs and custom label to the extra_context
        extra_context = extra_context or {}
        extra_context['logs'] = logs  # Add logs to the context
        extra_context['custom_logs_label'] = "(ADMIN)"  # Set custom label for the logs section
        
        return super().changelist_view(request, extra_context=extra_context)

class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('item', 'item_model', 'serial_number', 'action', 'timestamp')
    
from django.contrib import admin
from .models import Station  # Make sure to import the Station model








from django.contrib import admin
from .models import Station
from .forms import StationForm


class StationAdmin(admin.ModelAdmin):
    form = StationForm  # Use the custom form
    
    list_display = ('name', 'latitude', 'longitude', 'display_items')
    search_fields = ('name',)
    filter_horizontal = ('items',)

    def display_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()]) if obj.items.exists() else "No items"
    
    display_items.short_description = 'Attached Items'

    # Add the custom template for map integration
    change_list_template = "admin/inventory/station/change_list_with_map.html"  # For the list view
    change_form_template = "admin/inventory/station/change_form.html"
    
    def changelist_view(self, request, extra_context=None):
        # Pass your custom map context
        extra_context = extra_context or {}
        
        # Define map dimensions and name (you can customize these)
        extra_context['map'] = {
            'name': 'Station Map',
            'width': 2000,  # width of the map in pixels
            'height': 1000,  # height of the map in pixels
        }

        # Pass all stations to the context
        extra_context['stations'] = Station.objects.all()

        # Pass all lines to the context
        #extra_context['lines'] = Line.objects.all()  # Assuming you have a Line model that stores the drawn lines
        extra_context['lines'] = list(Line.objects.all().values('startX', 'startY', 'endX', 'endY', 'color'))
        #extra_context['lines'] = Line.objects.all().values('startX', 'startY', 'endX', 'endY', 'color')
        return super().changelist_view(request, extra_context=extra_context)

   
#class LineAdmin(admin.ModelAdmin):
  #  list_display = ('start_x', 'start_y', 'end_x', 'end_y', 'color', 'map')
class MapAdmin(admin.ModelAdmin):
    change_list_template = "admin/map_changelist.html"

    def changelist_view(self, request, extra_context=None):
        # Redirects to the map view
        return HttpResponseRedirect('/admin/map/')




# Register your models
admin.site.register(Station, StationAdmin)  # Register Station
admin.site.register(InventoryItem, InventoryItemAdmin)  # Register InventoryItem with custom admin
admin.site.register(InventoryLog, InventoryLogAdmin)
admin.site.register(StationLog)
admin.site.register(Line)