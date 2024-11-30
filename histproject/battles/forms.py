from django import forms

from histproject.battles.models import Battle, Country


class BattleBaseForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = '__all__'
        widgets ={
            'date': forms.DateInput(attrs={'placeholder': 'Y-M-d'}),
            'name': forms.TextInput(attrs={'placeholder': 'NAME battlefield'}),
            'latitude':forms.TextInput(attrs={'placeholder': '00.0000'}),
            'longitude':forms.TextInput(attrs={'placeholder': 'longitude'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://'}),
            'location': forms.TextInput(attrs={'placeholder': 'location'}),
            'description': forms.Textarea(attrs={'placeholder': 'description'})
        }

class BattleDetailForm(BattleBaseForm):
    pass

class BattleEditForm(BattleBaseForm):
    pass

class BattleDeleteForm(BattleBaseForm):
    pass

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields =('name',)