from django.contrib import admin
from places.models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase
from adminsortable2.admin import SortableTabularInline


class ImageInline(SortableTabularInline):
    model = Image

    readonly_fields = ("image_preview", )
    
    def image_preview(self, instance):
        maximum_height = 200
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url = instance.image.url,
            width = maximum_height*(instance.image.width/instance.image.height),
            height = maximum_height,
            )
        )

    def get_extra(self, request, obj=None, **kwargs):
        return 1

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):

    inlines = [
        ImageInline,
    ]
    

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass