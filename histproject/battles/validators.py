import re

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():  # Проверка дали стойността съдържа само букви
        raise ValidationError('Трябва да съдържа само букви.')


def clean_bg(value):
    if not isinstance(value, str):
        raise ValidationError('Трябва да бъде низ')



