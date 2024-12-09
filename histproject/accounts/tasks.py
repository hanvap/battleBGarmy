from celery import shared_task
from django.core.mail import send_mail
from histproject import settings
from django.contrib.auth import get_user_model

UserModel = get_user_model()
@shared_task
def send_welcome_email(email):
    send_mail(
        subject="New account created",
        message="Hello! Congrats on your new profile",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )