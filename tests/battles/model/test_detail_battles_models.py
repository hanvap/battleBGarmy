from django.test import TestCase
from django.core.exceptions import ValidationError

from histproject.battles.models import Country, Battle


# Импорт на модела Battle и Country

class BattleModelTests(TestCase):

    def setUp(self):
        # Създаване на тестова държава
        self.country = Country.objects.create(name='България')

    def test_battle_creation_successful(self):
        """ Проверете дали можете да създадете битка с валидни данни. """
        battle = Battle(
            name='Сражение',
            date='2024-01-01',
            location='София',
            result='Win',  # Предполага се, че 'WIN' е валиден избор
            description='Тестово описание.',
            latitude= 42.0,
            longitude= 23.0,
            image_url='http://example.com/image.jpg'
        )
        battle.full_clean()  # Проверка на валидността на данните
        battle.save()  # Записване на битката, преди добавяне на държави

        battle.countries_involved.add(self.country)  # След като е записана, добавяме страната
        self.assertEqual(battle.countries_involved.count(), 1)  # Проверка, че страната е добавена



    def test_battle_creation_invalid_name_not_string(self):
        """ Проверете дали получавате ValidationError, ако името не е низ. """
        battle = Battle(
            name=123,  # Неправилен тип данни
            date='2024-01-01',
            location='София',
            result='Win',
            description='Тестово описание.',
            latitude=42.0,
            longitude=23.0,
            image_url='http://example.com/image.jpg'
        )


        with self.assertRaises(ValidationError):
            battle.full_clean()  # Трябва да вдигне ValidationError


    def test_battle_creation_with_missing_fields(self):
        """ Проверете дали получавате ValidationError, ако липсват задължителни полета. """
        battle = Battle(
            name='',
            date=None,  # Липсва дата
            location='',
            result='',
            description='Тестово описание.',
            latitude=None,  # Липсва
            longitude=None,  # Липсва
            image_url='http://example.com/image.jpg'
        )


        with self.assertRaises(ValidationError):
            battle.full_clean()  # Трябва да вдигне ValidationError

    def test_battle_creation_invalid_coordinates(self):
        """ Проверете дали получавате ValidationError за невалидни координати. """
        battle = Battle(
            name='Сражение',
            date='2024-01-01',
            location='София',
            result='WIN',
            description='Тестово описание.',
            latitude=95.0,  # Невалидна стойност за latitude
            longitude=200.0,  # Невалидна стойност за longitude
            image_url='http://example.com/image.jpg'
        )


        with self.assertRaises(ValidationError):
            battle.full_clean()  # Трябва да вдигне ValidationError за координатите