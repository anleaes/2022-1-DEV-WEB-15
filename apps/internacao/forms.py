from django import forms
from .models import Internacao

class InternacaoForm(forms.ModelForm):

    class Meta:
        model = Internacao
        exclude = ('created_on' , 'updated_on',)