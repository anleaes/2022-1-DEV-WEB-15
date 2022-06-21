from django import forms
from .models import Client
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password' , 'email']

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('created_on' , 'updated_on',)

class UserChangeInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']        