from django.db import models
from tinymce.models import HTMLField


class Places(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    place_id = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='image', null=True)
    image_id = models.IntegerField(default=1, db_index=True, unique=True)
    places = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='img')

    def __str__(self):
        return f'{self.places} - {self.image_id}'

    class Meta:
        ordering = ['image_id']

