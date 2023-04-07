from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = HTMLField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='image')
    image_number = models.IntegerField(default=0, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='imgs')

    def __str__(self):
        return f'{self.place} - {self.image_number}'

    class Meta:
        ordering = ['image_number']


