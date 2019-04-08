from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class loginForm(forms.Form):
    '''An example form'''
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('invalid username or password.')
        return self.cleaned_data




