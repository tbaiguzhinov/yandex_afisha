from django.shortcuts import render
from places.models import Place

def start_page(request):
    geo_json = {
      "type": "FeatureCollection",
      "features": []}
    
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
            "detailsUrl": f"static/places/{place.placeid}.json"
          }
        }
      geo_json["features"].append(feature)
    context = {"geo_json": geo_json}
    return render(request, 'index.html', context)
