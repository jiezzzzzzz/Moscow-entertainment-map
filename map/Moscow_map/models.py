from django.db import models


class MapModels(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=500)
    text = models.TextField()
    coordinates_lng = models.CharField(max_length=200)
    coordinates_lat = models.CharField(max_length=200)
# Create your models here.
