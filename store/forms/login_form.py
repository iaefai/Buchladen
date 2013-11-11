from django import forms

class LoginForm(forms.Form):
    username = forms.EmailField()
    username.label = "e-mail"
    username.required = True
    password = forms.PasswordInput()
