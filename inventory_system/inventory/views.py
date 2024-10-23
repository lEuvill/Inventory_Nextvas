import json
from .models import Station
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Station, Map, Line, InventoryItem

def map_view(request):
    stations = Station.objects.all()
    context = {
        'map': {
            'name': 'Call Center Map',
            'width': 800,  # Define your map width
            'height': 600,  # Define your map height
        },
        'stations': stations,
    }
    return render(request, 'Maps/maps_view.html', context)
@csrf_exempt
def update_station(request, station_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            station = Station.objects.get(id=station_id)
            station.latitude = data['x']
            station.longitude = data['y']
            station.save()
            return JsonResponse({'status': 'success'})
        except Station.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Station not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
def admin_map_view(request):
    stations = Station.objects.all()
    return render(request, 'Maps/admin_map.html', {'stations': stations})

def update_station_coordinates(request, station_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            station = Station.objects.get(id=station_id)
            
            # Update the coordinates of the station
            station.latitude = data.get('y', station.latitude)
            station.longitude = data.get('x', station.longitude)
            station.save()

            return JsonResponse({'status': 'success', 'new_coordinates': {'x': station.longitude, 'y': station.latitude}})
        except Station.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Station not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
        

def station_change_view(request):
    map = Map.objects.first()  # Get the map object (or filter by a specific one)
    stations = Station.objects.all()  # Get all stations
    return render(request, 'path_to_your_template.html', {
        'map': map,
        'stations': stations
    })
    
 
def get_station_items(request, station_id):
    station = Station.objects.get(id=station_id)
    items = InventoryItem.objects.filter(station=station)  # Assuming InventoryItem has a ForeignKey to Station
    
    items_data = [{'name': item.name, 'quantity': item.quantity} for item in items]
    return JsonResponse({'items': items_data})
   
from .models import Line

@csrf_exempt
def save_line(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            startX = int(data['startX'])  
            startY = int(data['startY'])
            endX = int(data['endX'])
            endY = int(data['endY'])
            color = data['color']

            line = Line(startX=startX, startY=startY, endX=endX, endY=endY, color=color)
            line.save()

            return JsonResponse({'status': 'success', 'message': 'Line saved successfully'}, status=200)

        except Exception as e:
            logger.error(f"Error saving line: {str(e)}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)