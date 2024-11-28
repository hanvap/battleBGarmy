from django.urls import path

from histproject.common.views import home

urlpatterns = [
    path('', home, name='home'),
]