#authenticates users against the database

from django import forms
	class LoginForm(forms.Form):
    username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput) #passwordinput widget, renders HTML input element


