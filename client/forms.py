from django import forms

class LoginForm(forms.form):
    username = forms.CharField(label='Mail', max_length=100)
    password = forms.CharField(label='Mot de passe', max_length=100, widget=forms.PasswordInput)