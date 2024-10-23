from django import forms
from .models import Station, InventoryItem
from django.db.models import Q

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'latitude', 'longitude', 'items']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get all items that are assigned to any station, excluding the current station
        assigned_items = Station.objects.exclude(id=self.instance.id).values_list('items', flat=True)

        # Check if the Station instance has been saved (i.e., it has an ID)
        if self.instance.pk:
            # Include currently assigned items to this station
            current_items = self.instance.items.all()

            # Filter the queryset to show only items that are not assigned to another station or are already assigned to this one
            self.fields['items'].queryset = InventoryItem.objects.filter(
                Q(id__in=current_items) | ~Q(id__in=assigned_items)
            )
        else:
            # For new stations, exclude items already assigned to other stations
            self.fields['items'].queryset = InventoryItem.objects.exclude(id__in=assigned_items)

        # Ensure the field is not empty in the form (optional)
        if not self.fields['items'].queryset.exists():
            self.fields['items'].queryset = InventoryItem.objects.all()
