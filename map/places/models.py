from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200)
    text = models.TextField()
    coordinates_lng = models.CharField(max_length=200)
    coordinates_lat = models.CharField(max_length=200)
    place_id = models.CharField(max_length=25, unique=True)