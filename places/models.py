from django.db import models
from tinymce.models import HTMLField

class Place(models.Model):
    """Модель места."""
    title = models.CharField("Название", max_length=100)
    placeid = models.CharField("ID места", max_length=50)
    description_short = models.CharField("Короткое описание", max_length=500)
    description_long = HTMLField("Длинное описание")
    lng = models.FloatField("Широта")
    lat = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField("Картинка")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Место"
    )
    order_number = models.PositiveIntegerField(
        "Порядковый номер",
        default=0,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.order_number} {self.place}"

    class Meta:
        ordering = ['order_number']
