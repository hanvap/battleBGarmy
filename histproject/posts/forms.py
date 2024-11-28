from django import forms
from .models import Comment, Rating

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        labels = {
            'content': 'comment',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'comment'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EditCommentForm(CommentForm):
    pass

class DeleteCommentForm(CommentForm):
    pass

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']

        labels = {
            'score': 'оценка',
        }
        error_messages = {
            'error': 'между 1 и 5',
        }
        widgets = {
            'score': forms.TextInput(attrs={'placeholder': 'между 1 и 5'})
        }

