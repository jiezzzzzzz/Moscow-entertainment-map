from django.urls import path
from .views import start_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', start_page)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)