from django.contrib import admin
from django.contrib.auth import get_user_model

from histproject.accounts.models import Profile

UserModel = get_user_model()
@admin.register(UserModel)
class ModelNameAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_full_name']
    list_filter = ['first_name', 'last_name']
