from django.apps import AppConfig


class BookingsConfig(AppConfig):
    name = 'bookings'
    
    # Al arrancar la app, se importan las señales para que se registren los receptores de señales
    def ready(self):
        import bookings.signals 
