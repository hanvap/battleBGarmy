from django.urls import path
from .views import HistoricalEventCreateView, HistoricalEventListView, HistoricalEventDetailView

urlpatterns = [
    path('event/create/', HistoricalEventCreateView.as_view(), name='event_create'),
    path('events/', HistoricalEventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', HistoricalEventDetailView.as_view(), name='event_detail'),
]
