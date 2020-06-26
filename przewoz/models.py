from django.db import models
from django.contrib.auth.models import User

VEHICLE_CHOICES = ((1, 'tir'), (2, 'van'), (3, 'minivan'))
CARGO_CHOICES = ((1, 'europaleta'), (2, 'paleta'), (3, 'dłużyca'))


# Create your models here.
class Vehicle(models.Model):
    brand = models.CharField(max_length=40)
    type = models.CharField(max_length=24, choices=VEHICLE_CHOICES, default='tir')
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    volume = models.FloatField()
    max_capacity = models.FloatField()
    max_length = models.FloatField()
    description = models.TextField()


class Transit(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    departure = models.DateTimeField(auto_now_add=True, blank=True)
    arrival = models.DateTimeField(auto_now_add=True, blank=True)
    destination = models.CharField(max_length=64)
    place_of_departure = models.CharField(max_length=64)
    description = models.TextField()

# DATETIME PICKER BOOTSTRAP

class Cargo(models.Model):
    type = models.CharField(max_length=64, choices=CARGO_CHOICES)
    dimensions = models.CharField(max_length=64, default='120, 80, 14.4')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_vehicle = models.ForeignKey(Vehicle, default='', on_delete=models.CASCADE)
    assigned_transit = models.ForeignKey(Transit, default='', on_delete=models.CASCADE)
    description = models.TextField()
