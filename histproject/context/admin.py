from django.contrib import admin

from histproject.context.models import Video, HistoricalEvent


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'yuotube_id')
    list_filter = ['yuotube_id']


@admin.register(HistoricalEvent)
class HistoricalEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'date')


