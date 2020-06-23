from django.db import models
from django.contrib.auth.models import User

VEHICLE_CHOICES = ('tir', 'van', 'minivan')
CARGO_CHOICES = ('paleta', 'dłużyca')


# Create your models here.
# class Vehicle(models.Model):
#     brand = models.CharField(max_length=40)
#     type = models.CharField(max_length=24, choices=VEHICLE_CHOICES, default='tir')
#     driver = models.ForeignKey(User, on_delete=models.CASCADE)
#     volume = models.FloatField()
#     max_capacity = models.FloatField()
#     max_length = models.FloatField()
#
#
# class Transit(models.Model):
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
#     departure = models.DateTimeField()
#     arrival = models.DateTimeField()
#     destination = models.CharField(max_length=64)
#     place_of_departure = models.CharField(max_length=64)
#
#
# class Cargo(models.Model):
#     type = models.CharField(max_length=64, choices=CARGO_CHOICES)
#     if type == 'paleta':
#         dimensions = models.CharField(max_length=64, default='120, 80, 14.4')
#     dimensions = models.CharField(max_length=64)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     assigned_vehicle = models.ForeignKey(Vehicle, default='')
#     assigned_transit = models.ForeignKey(Transit, default='')