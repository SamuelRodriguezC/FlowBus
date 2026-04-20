from django.contrib import admin
from .models import Bus, Seat

class BusAdmin(admin.ModelAdmin): 
    list_display = ('bus_name', 'number', 'origin', 'destination')
    search_fields = ('bus_name', 'number', 'origin', 'destination')
    list_filter = ('origin', 'destination')
    
    
# Register your models here.
admin.site.register(Bus, BusAdmin)


admin.site.register(Seat)
