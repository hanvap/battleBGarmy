from django.db import models


class ChoiceResult(models.TextChoices):
    WIN = 'Win', 'Победа за БА',
    LOSS = 'Loss', 'Загуба за БГ',