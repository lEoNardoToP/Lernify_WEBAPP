from django.contrib.auth.decorators import login_required
from Startpages.models import CreateAccountForm, LoginForm, ResetPasswordForm
from Startpages.models import ForgotPasswordForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render
def HomePage(request):
    return render(request, "Home.html")

def LoginPage(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login")
            else :
                context["error"] = "Invalid Username or Password"
    else :
        form = LoginForm()
    context["form"] = form
    return render(request, "LoginPage.html", context)

def CreateAccount(request):
    context = {}
    if request.method == "POST":
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            existsEmail = User.objects.filter(email=request.POST['email']).exists()
            if user is None and not existsEmail:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect("login")
            elif existsEmail :
                context["error"] = "Email already exists"
            elif user is not None:
                context["error"] = "User already exists"
    else :
        form = CreateAccountForm()
    context["form"] = form
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