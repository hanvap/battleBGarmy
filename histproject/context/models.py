from django.db import models

from django.db import models

class HistoricalEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    yuotube_id = models.CharField(max_length=100)
    historical_event = models.ForeignKey(HistoricalEvent, on_delete=models.CASCADE, related_name='videos')

    def __str__(self):
        return self.title