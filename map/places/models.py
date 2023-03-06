from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.FloatField(max_length=200)
    lat = models.FloatField(max_length=200)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='image')
    image_number = models.IntegerField()
    places = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='imgs')

    def __str__(self):
        return f'{self.places} - {self.image_number}'

    class Meta:
        ordering = ['image_number']

