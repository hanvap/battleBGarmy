from cProfile import label

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    first_name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        error_messages= {'blank': 'Името е задължително'},

    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        error_messages= {'blank': 'Фамилията е задължителна'},
    )
    data_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    profile_picture = models.URLField(
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
