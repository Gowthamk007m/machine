# models.py
from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.code

class AirportRoute(models.Model):
    POSITION_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )

    from_airport = models.ForeignKey(Airport, related_name='routes_from', on_delete=models.CASCADE)
    to_airport = models.ForeignKey(Airport, related_name='routes_to', on_delete=models.CASCADE)
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    duration = models.IntegerField(help_text="Distance in km")

    def __str__(self):
        return f"{self.from_airport} -> {self.to_airport} ({self.position}, {self.duration} km)"
