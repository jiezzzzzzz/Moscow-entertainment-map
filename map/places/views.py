from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def convert_in_json(location):
    serialized = {"type": "Feature",
                  "geometry": {
                               "type": "Point",
                               "coordinates": [location.lng, location.lat]
                                },
                  "properties": {
                               "title": location.title,
                               "placeId": location.id,
                               "detailsUrl": (reverse("places", args=(location.id,)))
                                }
                  }

    return serialized


def start_page(request):
    locations = Place.objects.all()
    context = {
        "data": {
            "type": "FeatureCollection",
            "features": [convert_in_json(location) for location in locations]
        }
    }
    return render(request, 'index.html', context=context)


def get_place_details(request, place_id):
    place_object = get_object_or_404(Place, pk=place_id)
    place_images = place_object.imgs.all()

    context = {
        "title": place_object.title,
        "imgs": [img.image.url for img in place_images],
        "description_short": place_object.description_short,
        "description_long": place_object.description_long,
        "coordinates": {
            "lng": place_object.lng,
            "lat": place_object.lat
        }
    }
    return JsonResponse(context, json_dumps_params={'ensure_ascii': False, 'indent': 2})