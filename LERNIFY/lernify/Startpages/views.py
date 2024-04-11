from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def HomePage(request):
    return render(request, "Home.html")

def LoginPage(request):
    return render(request, "LoginPage.html")

def CreateAccount(request):
    return render(request, "CreateAccount.html")

def ForgotPassword(request):
    return render(request, "ForgotPassword.html")