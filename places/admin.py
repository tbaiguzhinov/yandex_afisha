"""Админка проекта places."""
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Image, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    """Модель изображения."""

    model = Image

    readonly_fields = ("image_preview", )

    def image_preview(self, instance):
        """Превью изображения."""
        maximum_height = "200px"
        return format_html(
            '<img style="max-height:{};" src="{}"/>',
            maximum_height,
            instance.image.url,
            )

    def get_extra(self, request, obj=None, **kwargs):
        """Уменьшаем число дополнительных форм до 1."""
        return 1


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    """Модель места."""

    inlines = [ImageInline, ]

    search_fields = ['title', ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Модель изображения."""

    autocomplete_fields = ["place", ]
