from django.db import models

# Create your models here.
class Bus(models.Model):
    Busno=models.IntegerField()
    Departure_Time=models.CharField(max_length=8)
    Destinations=models.CharField(max_length=500)
    Seats_Available=models.IntegerField()
    TicketCosts=models.CharField(max_length=500)
    #overriding __str__ function
    def __str__(self):
        return str(self.Busno)+" "+self.Departure_Time+" "+self.Destinations+" "+str(self.Seats_Available)+" "+self.TicketCosts

class Ticket(models.Model):
    busno=models.IntegerField()
    destination=models.CharField(max_length=50)
    no_of_persons=models.IntegerField()
    #overriding __str__ function
    def __str__(self):
        return str(self.busno)+" "+self.destination+" "+str(self.no_of_persons)
