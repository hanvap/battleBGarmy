from django.contrib import admin

from histproject.social_share.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_filter = ['title']

