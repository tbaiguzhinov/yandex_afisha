"""Views for places project."""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def create_start_page(request):
    """Start page."""
    data = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()
    for place in places.iterator():
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.placeid,
                "detailsUrl": reverse('places', args=[place.id]),
            }
        }
        data["features"].append(feature)
    context = {"geo_json": data}
    return render(request, 'index.html', context)


def get_place(request, place_id):
    """Return JSON with place description."""
    place = get_object_or_404(Place, id=place_id)
    content = {
      "title": place.title,
      "imgs": [image.image.url for image in place.images.all()],
      "description_short": place.description_short,
      "description_long": place.description_long,
      "coordinates": {
        "lat": place.lat,
        "lng": place.lng,
        },
    }
    response = JsonResponse(
        content,
        json_dumps_params={
            'ensure_ascii':
            False,
            'indent': 4
        }
    )
    return response
