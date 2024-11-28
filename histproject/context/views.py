from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import HistoricalEventForm
from .models import HistoricalEvent

class HistoricalEventCreateView(CreateView):
    model = HistoricalEvent
    form_class = HistoricalEventForm
    template_name = 'context/event_form.html'
    success_url = reverse_lazy('event_list')

class HistoricalEventListView(ListView):
    model = HistoricalEvent
    template_name = 'context/event_list.html'
    context_object_name = 'events'

class HistoricalEventDetailView(DetailView):
    model = HistoricalEvent
    template_name = 'context/event_detail.html'
    context_object_name = 'event'