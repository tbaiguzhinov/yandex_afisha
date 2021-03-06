import os
import time

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place


class Command(BaseCommand):
    """Обработчик команды load_places."""

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
                'description_short': content['description_short'],
                'description_long': content['description_long'],
            }
        )
        if not created:
            return
        for order_number, image_link in enumerate(
            content['imgs'],
            start=1
        ):
            file_name = os.path.split(image_link)[-1]
            try:
                response = requests.get(image_link)
                response.raise_for_status()
                content = ContentFile(response.content)
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
