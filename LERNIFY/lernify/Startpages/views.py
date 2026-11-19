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
            if "ricordami" in request.POST :
                remember_me = request.POST['ricordami']
            else :
                remember_me = False
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return redirect("Startpages:login")
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
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            if password != form.cleaned_data["confirmPassword"]:
                context["error"] = "Passwords do not match"
            elif User.objects.filter(username=username).exists():
                context["error"] = "User already exists"
            elif User.objects.filter(email__iexact=email).exists():
                context["error"] = "Email already exists"
            else:
                # The email must be stored: password reset looks users up by it.
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect("Startpages:login")
    else :
        form = CreateAccountForm()
    context["form"] = form
    return render(request, "CreateAccount.html", context)
