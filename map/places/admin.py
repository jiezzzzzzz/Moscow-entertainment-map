from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview']

    def get_preview(self, object):
        return mark_safe(f'<img src="{object.image.url}" height=200>')


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
