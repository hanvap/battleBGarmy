from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'histproject.settings')  # заменете с името на вашия проект
app = Celery('histproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()