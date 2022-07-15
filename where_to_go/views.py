from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from places.models import Place
from django.urls import reverse

def start_page(request):
    geo_json = {
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
        geo_json["features"].append(feature)
    context = {"geo_json": geo_json}
    return render(request, 'index.html', context)

def get_place(request, place_id):
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
    response = JsonResponse(content, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    return response