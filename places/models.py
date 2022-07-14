from django.db import models

class Place(models.Model):
    """Модель места."""
    title = models.CharField("Название", max_length=100)
    description_short = models.CharField("Короткое описание", max_length=500)
    description_long = models.TextField("Длинное описание")
    lng = models.FloatField("Широта")
    lat = models.FloatField("Долгота")

    def __str__(self):
        return self.title
