from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from histproject.accounts.mixins import DisableFieldsMixin
from histproject.accounts.models import Profile


class CustomUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    widgets = {
       'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
       'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
       'data_of_birth': forms.DateInput(attrs={'placeholder': 'Y-M-D'}),
       'profile_picture': forms.URLInput(attrs={'placeholder': 'https://'}),
       'email': forms.EmailInput(attrs={'placeholder': 'email'})

    }


class ProfileDeleteForm(ProfileForm, DisableFieldsMixin):
    disabled_fields = ('first_name', 'last_name','data_of_birth', 'profile_picture')

