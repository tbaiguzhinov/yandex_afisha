from django.contrib import admin
from places.models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

    def get_extra(self, request, obj=None, **kwargs):
        return 1

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass