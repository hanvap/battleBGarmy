from django.db import models

from histproject.battles.choices import ChoiceResult
from histproject.battles.validators import validate_only_letters, clean_bg


class Country(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Име',
        validators=[clean_bg]
    )



    def __str__(self):
        return self.name


class Battle(models.Model):
    name = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )
    date = models.DateField()
    location = models.CharField(max_length=200)
    countries_involved = models.ManyToManyField(
        to=Country,
        related_name="countries"
    )
    result = models.CharField(
        max_length=100,
        choices=ChoiceResult.choices
    )  # "Win" или "Loss"
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Поле за ширина
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Поле за дължина
    image_url = models.URLField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} ({self.date})"