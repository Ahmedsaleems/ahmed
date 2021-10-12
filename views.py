from django.shortcuts import render
from .models import flight, passenger
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": flight.objects.all()
    })
def flightt(request, flight_id):
    f = flight.objects.get(id=flight_id)
    return render(request, "flights/flight.html", {
        "flight1": f, "passengers": f.passengers.all(),
        "nonpassenger": passenger.objects.exclude(allflights=f).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        e = flight.objects.get(id=flight_id)
        passng = passenger.objects.get(id=int(request.POST["passeng"]))
        passng.allflights.add(e)
        return HttpResponseRedirect(reverse("flight", args=(e.id,)))