from django import forms
from .models import Raca

class RacaForm(forms.ModelForm):

    class Meta:
        model = Raca
        exclude = ('created_on' , 'updated_on',)