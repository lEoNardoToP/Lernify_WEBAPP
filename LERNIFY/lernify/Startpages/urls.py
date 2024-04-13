from django.contrib import admin
from django.urls import path, reverse_lazy
from Startpages import views
from django.contrib.auth import views as auth_views
from Startpages.models import ResetPasswordForm

appname = 'Startpages'

urlpatterns = [

    path("",  views.HomePage, name="home"),
    path("Login", views.LoginPage, name="login"),
    path("Registration", views.CreateAccount, name="registration"),
    path("ForgotPassword", auth_views.PasswordResetView.as_view(template_name="ForgotPassword.html", email_template_name="EMAIL_RESET_PASSWORD.txt", success_url = reverse_lazy("Startpages:password_reset_done")), name="forgot_password"),
    path("PasswordResetDone", auth_views.PasswordResetDoneView.as_view(template_name="PasswordResetDone.html"), name="password_reset_done"),
    path('ResetPassword/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="ResetPassword.html", form_class=ResetPasswordForm, success_url=reverse_lazy("Startpages:password_reset_complete")), name="password_reset_confirm"),
    path("PasswordResetomplete", views.LoginPage, name="password_reset_complete"),

]