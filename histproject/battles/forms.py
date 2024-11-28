from django import forms

from histproject.battles.models import Battle


class BattleBaseForm(forms.ModelForm):
    class Meta:
        model = Battle
        fields = '__all__'

class BattleDetailForm(BattleBaseForm):
    pass

class BattleEditForm(BattleBaseForm):
    pass

class BattleDeleteForm(BattleBaseForm):
    pass