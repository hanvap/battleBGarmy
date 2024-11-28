from django import forms
from .models import HistoricalEvent

class HistoricalEventForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ['title', 'description', 'date', 'image', 'video_url']