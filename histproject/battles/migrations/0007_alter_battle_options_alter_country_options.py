# Generated by Django 5.1.3 on 2024-11-29 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battles', '0006_alter_battle_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='battle',
            options={'ordering': ('date',)},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': ('name',)},
        ),
    ]
