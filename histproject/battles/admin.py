from django.contrib import admin
from .models import Battle, Country


class BattleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'result', 'latitude', 'longitude', 'image_url')
    fields = ('name', 'date', 'location', 'countries_involved', 'result', 'description', 'latitude', 'longitude')

admin.site.register(Battle, BattleAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Полета, които искате да показвате в списъка
    search_fields = ('name',)  # Позволява търсене по име

# Регистрирайте модела Country с CountryAdmin
admin.site.register(Country, CountryAdmin)
