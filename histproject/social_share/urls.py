from django.urls import path

from histproject.social_share.views import post_detail, PostCreateView

urlpatterns = [
    path('post/', post_detail, name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
]