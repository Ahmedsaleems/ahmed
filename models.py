from django.db import models

# Create your models here.
class airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    def __str__(self):
        return f"{self.city} ({self.code})"


class flight(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrivals")
    destination = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departures")
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.id}:{self.origin} to {self.destination} in {self.duration}"

class passenger(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    allflights = models.ManyToManyField(flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.firstname} {self.lastname}"