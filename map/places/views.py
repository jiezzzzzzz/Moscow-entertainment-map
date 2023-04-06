from django.shortcuts import render
from .models import Place, Image
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import sqlite3


def convert_in_json(location):
    serialized = {"type": "Feature",
                  "geometry": {
                               "type": "Point",
                               "coordinates": [location.lng, location.lat]
                                         },
                  "properties": {
                               "title": location.title,
                               "placeId": location.id,
                               "detailsUrl": f"http://127.0.0.1:8000/places/{location.id}/"
                           }
                  }

    return serialized


def start_page(request):
    locations = Place.objects.all()
    context = {}
    context['data'] = {
            "type": "FeatureCollection",
            "features": [convert_in_json(location) for location in locations]}
    return render(request, 'index.html', context=context)


def place_details(request, place_id):
    object = get_object_or_404(Place, pk=place_id)
    place_images = object.imgs.all()
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()

    cursor.execute("SELECT * from sqlite_master where type = 'Place'")
    print(cursor.fetchall())
    print(place_images)

    context = {
        'title': object.title,
        'imgs': [img.image.url for img in place_images],
        'description_short': object.description_short,
        'description_long': object.description_long,
        'coordinates': {
            'lng': object.lng,
            'lat': object.lat
        }
    }
    return JsonResponse(context, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})