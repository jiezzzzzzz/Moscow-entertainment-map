from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse


def serialize_location(location):
    serialized_location = {'type': 'Feature',
                  'geometry': {
                               'type': 'Point',
                               'coordinates': [location.lng, location.lat]
                  },
                  'properties': {
                               'title': location.title,
                               'placeId': location.id,
                               'detailsUrl': (reverse('places', args=(location.id,)))
                  }
    }

    return serialized_location


def start_page(request):
    locations = Place.objects.all()
    context = {
        'data': {
            'type': 'FeatureCollection',
            'features': [serialize_location(location) for location in locations]
        }
    }
    return render(request, 'index.html', context=context)


def get_place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_images = place.imgs.all()

    context = {
        'title': place.title,
        'imgs': [img.image.url for img in place_images],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(context, json_dumps_params={'ensure_ascii': False, 'indent': 2})
