# Generated by Django 5.0.4 on 2024-11-13 13:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(error_messages='Името е задължително', max_length=40)),
                ('last_name', models.CharField(error_messages='Фамилията е задължителна', max_length=50)),
                ('data_of_birth', models.DateField(blank=True, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
