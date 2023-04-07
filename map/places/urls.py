from django.urls import path
from .views import start_page, get_place_details


urlpatterns = [
    path('', start_page),
    path('places/<int:place_id>/', get_place_details, name='places')
]
