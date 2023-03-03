from django.contrib import admin
from .models import Places, Image
from django.utils.safestring import mark_safe

admin.site.register(Image)


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview']

    def preview(self, object):
        return mark_safe(f'<img src="{object.image.url}" height=200>')


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
