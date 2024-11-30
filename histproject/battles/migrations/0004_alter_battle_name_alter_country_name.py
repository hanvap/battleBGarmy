# Generated by Django 5.1.3 on 2024-11-29 11:28

import histproject.battles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0003_battle_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='name',
            field=models.CharField(max_length=200, validators=[histproject.battles.validators.clean_bg, histproject.battles.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, unique=True, validators=[histproject.battles.validators.clean_bg, histproject.battles.validators.validate_only_letters], verbose_name='Име'),
        ),
    ]