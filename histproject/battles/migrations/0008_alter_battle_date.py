# Generated by Django 5.1.3 on 2024-11-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0007_alter_battle_options_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='date',
            field=models.DateField(),
        ),
    ]
