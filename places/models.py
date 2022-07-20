"""Models for places project."""
from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    """Модель места."""

    title = models.CharField("Название", max_length=100, db_index=True)
    placeid = models.CharField("ID места", max_length=50, unique=True)
    description_short = models.TextField("Короткое описание", max_length=500)
    description_long = HTMLField("Длинное описание")
    lng = models.FloatField("Широта")
    lat = models.FloatField("Долгота")

    def __str__(self):
        return self.title


class Image(models.Model):
    """Модель изображения."""

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
        db_index=True,
    )

    class Meta:
        ordering = ['order_number']

    def __str__(self):
        return f"{self.order_number} {self.place}"
