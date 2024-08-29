from django.contrib import admin
from .models import Bus
# Register your models here.

#admin.site.register(Bus)

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display=('Busno','Departure_Time','Destinations','Seats_Available','TicketCosts')
    list_filter=('Departure_Time',)
    searching=('Busno',)
    ordering=('Departure_Time',)
