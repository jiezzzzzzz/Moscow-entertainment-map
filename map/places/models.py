from django.db import models
import PIL


class Places(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=200)
    text = models.TextField()
    coordinates_lng = models.CharField(max_length=200)
    coordinates_lat = models.CharField(max_length=200)
    place_id = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='image', null=True)
    image_id = models.IntegerField(null=True)
    places = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='img')

    def __str__(self):
        return f'{self.places} - {self.image_id}'
