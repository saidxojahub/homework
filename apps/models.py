# models.py
from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    avatar = models.URLField()

    def __str__(self):
        return self.name