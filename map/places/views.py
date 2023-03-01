from django.shortcuts import render
from .models import Places


def convert_in_json(location):
    serialized = {"type": "Feature",
                           "geometry": {
                               "type": "Point",
                               "coordinates": [location.coordinates_lng, location.coordinates_lat]
                           },
                           "properties": {
                               "title": location.title,
                               "placeId": location.place_id,
                               "detailsUrl": ""
                           }
                           }
    return serialized


def start_page(request):
    locations = Places.objects.all()
    context = {}
    context['data'] = {
            "type": "FeatureCollection",
            "features": [convert_in_json(location) for location in locations]}
    return render(request, 'index.html', context=context)
