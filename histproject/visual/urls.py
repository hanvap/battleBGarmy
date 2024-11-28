from django.urls import path
from .views import statistics_view, battle_map_view

urlpatterns = [
    path('', statistics_view, name='statistics'),
    path('map/', battle_map_view, name='battle_map'),
]