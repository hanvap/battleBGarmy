from django.db import models
from django.shortcuts import render

import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from django.http import HttpResponse

import folium

from histproject.battles.models import Battle


def statistics_view(request):
    # Графика за брой битки по години
    battles_by_year = Battle.objects.extra(select={'year': 'EXTRACT(YEAR FROM date)'}).values('year').annotate(
        count=models.Count('id')).order_by('year')

    years = [battle['year'] for battle in battles_by_year]
    counts = [battle['count'] for battle in battles_by_year]

    plt.figure(figsize=(10, 6))
    plt.bar(years, counts, color='red')
    plt.xlabel('Година')
    plt.ylabel('Брой битки')
    plt.title('Брой битки по години')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()
    statistics_image = base64.b64encode(image_png).decode('utf-8')

    # Интерактивна карта
    m = folium.Map(location=[20, 0], zoom_start=2)

    for battle in Battle.objects.all():
        folium.Marker(
            location=[battle.latitude, battle.longitude],  # Предполага, че имате гео данни
            popup=battle.name,
        ).add_to(m)

    map_html = m._repr_html_()

    context = {
        'statistics_image': statistics_image,

    }

    return render(request, 'battles/statistics.html', context)




def battle_map_view(request):
    # Създайте карта, центрирана на произволна позиция
    m = folium.Map(location=[20, 0], zoom_start=2)

    # Добавете маркери за всяка битка
    for battle in Battle.objects.all():
        image_html = f"<img src='{battle.image_url}' style='width: 100%; height: auto;'>" if battle.image_url else ""
        folium.Marker(
            location=[battle.latitude, battle.longitude],
            popup=folium.Popup(f"<strong>{battle.name}</strong><br>Date: {battle.date}<br>Result: {battle.result}<br>{image_html}", max_width=300),
            icon=folium.Icon(color='blue')
        ).add_to(m)

    # Генерирайте HTML кода за картата
    map_html = m._repr_html_()

    context = {
        'map_html': map_html,
    }

    return render(request, 'visual/battle_map.html', context)
