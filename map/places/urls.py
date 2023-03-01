from django.urls import path
from .views import start_page, place_details


urlpatterns = [
    path('', start_page),
    path('places/<int:place_id>/', place_details)
]
