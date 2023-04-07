from django.contrib import admin
from .models import Place, Image
from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.utils.html import format_html


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, object):
        return format_html('<img src="{}" height={}>',
                           object.image.url, '200')


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
