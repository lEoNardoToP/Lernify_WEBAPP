from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


# Create your models here.

class CreateAccountForm(forms.Form):
    username = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(
        attrs={'class': 'distanziati', 'id': 'nome', 'placeholder': 'nome'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'distanziati', 'id': 'email', 'placeholder': 'email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'distanziati', 'id': 'password', 'placeholder': 'password'}))
    confirmPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(
        attrs={'class': 'distanziati', 'id': 'confirmPassword', 'placeholder': 'Confirm Password'}))


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'id': 'email', 'placeholder': 'Inserisci qui la tua email...'}))


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'id': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'id': 'password', 'placeholder': 'password'}))
    ricordami = forms.BooleanField(label="Ricordami", required=False,
                                   widget=forms.CheckboxInput(attrs={'id': 'Ricordami'}))


class ResetPasswordForm(auth_forms.SetPasswordForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__( user, *args, **kwargs)
        self.fields['new_password1'].label = 'New Password'
        self.fields['new_password2'].label = 'Confirm New Password'
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={"id":"password"})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={"id":"repeatPassword"})
        self.fields['new_password1'].help_text = ''
        self.fields['new_password2'].help_text = ''