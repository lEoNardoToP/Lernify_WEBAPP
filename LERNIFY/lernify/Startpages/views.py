from django.contrib.auth.decorators import login_required
from Startpages.models import CreateAccountForm, LoginForm, ResetPasswordForm
from Startpages.models import ForgotPasswordForm
from django.contrib.auth import login, logout
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def HomePage(request):
    return render(request, "Home.html")

def LoginPage(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            pass
    else :
        form = LoginForm()
    context = {"form": form}
    return render(request, "LoginPage.html", context)

def CreateAccount(request):
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            pass
    else :
        form = CreateAccountForm()
    context = {"form": form}
    return render(request, "CreateAccount.html", context)

def ForgotPassword(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            pass
    else :
        form = ForgotPasswordForm()
    context = {"form": form}
    return render(request, "ForgotPassword.html", context)

#@login_required(login_url="LoginPage")
def ResetPassword(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            pass
    else :
        form = ResetPasswordForm()
    context = {"form": form}
    return render(request, "ResetPassword.html", context)