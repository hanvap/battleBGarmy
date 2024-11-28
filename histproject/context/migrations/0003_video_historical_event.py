# Generated by Django 5.1.3 on 2024-11-22 14:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='historical_event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='context.historicalevent'),
            preserve_default=False,
        ),
    ]
