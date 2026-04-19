from django.db import models

# Create your models here.
class Bus(models.Model): 
    bus_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20, unique = True)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    features =  models.TextField()
    start_time = models.TimeField()
    reach_time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
class Seat(models.Model):
    bus = models.ForeignKey('Bus', on_delete=models.CASCADE, related_name='seats')
    seat_numer = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)