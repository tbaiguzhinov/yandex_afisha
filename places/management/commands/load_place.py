from django.core.management.base import BaseCommand
import requests
import uuid
import os

from places.models import Place, Image
from django.core.files.base import ContentFile


def load_image(image_link):
    response = requests.get(image_link)
    response.raise_for_status()
    return response.content


class Command(BaseCommand):
    help = 'Добавляет место Place по заданной ссылке формата .json'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_link',
            type=str,
            help='Json link to a place to be added',
        )


    def handle(self, *args, **options):
        response = requests.get(
            url=options['json_link']
        )
        response.raise_for_status()
        content = response.json()
        
        place, created = Place.objects.get_or_create(
            title=content['title'],
            lng=content['coordinates']['lng'],
            lat=content['coordinates']['lat'],
            defaults={
                'placeid': uuid.uuid4(),
                'description_short': content['description_short'],
                'description_long': content['description_long'],
            }
        )
        if created:
            for order_number, image_link in enumerate(content['imgs'], start=1):
                file_name = os.path.split(image_link)[-1]
                try:
                    content = ContentFile(load_image(image_link))
                except requests.HTTPError:
                    print("Страница не существует: ", image_link)
                    continue
                except requests.ConnectionError:
                    print("Проблемы с подключением")
                    time.sleep(5)
                    continue
                                
                image = Image.objects.create(
                    place=place,
                    order_number=order_number,
                )
                image.image.save(file_name, content, save=True)
