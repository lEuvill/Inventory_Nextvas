# inventory_system/urls.py
from django.contrib import admin
from django.urls import path
from inventory.views import map_view
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', map_view, name='map-view'),
    path('map/', views.map_view, name='map'),
    path('station/<int:station_id>/change/', views.station_change_view, name='station_change_view'),
    path('update-station/<int:station_id>/', views.update_station, name='update_station'),
    path('admin/map/', views.admin_map_view, name='admin_map'),
    path('update-station/<int:station_id>/', views.update_station_coordinates, name='update_station_coordinates'),
    path('save-line/', views.save_line, name='save_line'),
    path('get-station-items/<int:station_id>/', views.get_station_items, name='get_station_items'),
]
