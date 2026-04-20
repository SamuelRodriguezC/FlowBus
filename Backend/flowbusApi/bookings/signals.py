from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Bus, Seat


@receiver(post_save, sender=Bus) # Al crear un objeto bus se ejecuta esta función
def create_seats_for_bus(sender, instance, created, **kwargs): #crear automáticamente en la tabla seats los asientos de un bus
    if created: # si se ha creado un nuevo bus
        for i in range(1, instance.total_seats +1): # crear asientos desde 1 hasta el número total de asientos del bus
            Seat.objects.create(bus=instance, seat_number= f"S{i}") # Crea cada asiento y le asigna el bus, y el número de asiento (S1, S2)