from django import forms

from histproject.social_share.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'