"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from przewoz import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('transits/', views.TransitView.as_view(), name='transits'),# ADD TRANSIT
    path('vehicles/', views.VehicleView.as_view(), name='vehicles'), # ADD VEHICLE
    path('cargo/', views.CargoView.as_view(), name='cargo'), # ADD CARGO
    path('search_transit/',views.SearchTransitView.as_view(), name='searchTransit' ),
    path('search_transit/make_reservation/<int:pk>', views.MakeReservationView.as_view(), name='makeReservation'),
    path('my_reservations/', views.MyReservationsView.as_view(), name='myReservation'),
    path('my_vehicles/', views.MyVehiclesView.as_view(), name='myVehicles'),
    path('my_transits/', views.MyTransitsView.as_view(), name='myTransits'),
    path('my_cargo/', views.MyCargoView.as_view(), name='myCargo'),
    path('my_vehicles/delete_vehicle/<int:pk>', views.DeleteVehicleView.as_view(), name='deleteVehicle'),
    path('my_transits/delete_transit/<int:pk>', views.DeleteTransitView.as_view(), name='deleteTransit'),
    path('my_cargo/delete_cargo/<int:pk>', views.DeleteCargoView.as_view(), name='deleteCargo'),
    path('my_vehicles/update_vehicle/<int:pk>', views.UpdateVehicleView.as_view(), name='updateVehicle'),
    path('my_transits/update_transit/<int:pk>', views.UpdateTransitView.as_view(), name='updateTransit'),
    path('my_cargo/update_cargo/<int:pk>', views.UpdateCargoView.as_view(), name='updateCargo'),
]
