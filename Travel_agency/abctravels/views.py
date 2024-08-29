from django.shortcuts import render
from .models import Bus,Ticket
from django.http import HttpResponseRedirect,HttpResponse
from .forms import Ticket_form
# Create your views here.

def book(request):
    buslist=Bus.objects.all()
    ticket=Ticket_form()
    flag=0
    if request.method=="POST":
        ticket=Ticket_form(request.POST)
        if ticket.is_valid():
            no=Ticket.no_of_persons
            av=Bus.objects.get(Busno=Ticket.busno)
            avseat=av.Seats_Available
            if avseat-no>=0:
                av.Seats_Available-=no
                av.save()
                Ticket.save()
                flag=1
                return HttpResponseRedirect('/Result/')
    return render(request,"booking.html",context={"flag":flag,"ticket":ticket,"buslist":buslist})

def result(request):
    ticket=Ticket_form()
    av=Bus.objects.get(Busno=Ticket.busno)
    destlist=av.Destinations.split(',')
    costlist=av.TicketCosts.split(',')
    for i in len(destlist):
        if destlist[i]==Ticket.destination:
            cost=costlist[i]
            m="Ticket is booked \n Total Price is Rs."+cost
            return HttpResponse(m)
    return HttpResponse("Not Booked")

            
            
