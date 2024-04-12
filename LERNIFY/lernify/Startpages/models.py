from django.db import models
from django import forms


# Create your models here.

class CreateAccountForm(forms.Form) :
    username = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'class' :'distanziati', 'id' : 'nome', 'placeholder':'nome'}))
    email = forms.EmailField(label='Email' , widget=forms.EmailInput(attrs={'class' :'distanziati', 'id' : 'email', 'placeholder':'email'}))
    password = forms.CharField(label= "Password", widget=forms.PasswordInput(attrs={'class' :'distanziati', 'id' : 'password', 'placeholder':'password'}))
    confirmPassword = forms.CharField(label= "Confirm Password", widget=forms.PasswordInput(attrs={'class' :'distanziati', 'id' : 'confirmPassword', 'placeholder':'Confirm Password'}))

class ForgotPasswordForm(forms.Form) :
    email = forms.EmailField(label='Email' , widget=forms.EmailInput(attrs={'id' : 'email', 'placeholder':'Inserisci qui la tua email...'}))

class LoginForm(forms.Form) :
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={ 'id': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={ 'id': 'password', 'placeholder': 'password'}))
    Ricordami = forms.BooleanField(label="Ricordami", required="false", widget=forms.CheckboxInput(attrs={'id':'Ricordami'}))

class ResetPasswordForm(forms.Form) :
    password = forms.CharField(label="Nuova Password", widget=forms.PasswordInput(
        attrs={'id': 'password', 'placeholder': 'Inserisci la nuova password...'}))
    confirmPassword = forms.CharField(label="Conferma Password", widget=forms.PasswordInput(
        attrs={ 'id': 'RepeatPassword', 'placeholder': 'Conferma la tua password...'}))