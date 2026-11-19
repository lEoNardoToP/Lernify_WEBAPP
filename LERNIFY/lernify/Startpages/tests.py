from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase, override_settings
from django.urls import reverse

LOCMEM = "django.core.mail.backends.locmem.EmailBackend"


def signup(client, username="ada", email="ada@example.com", password="Str0ng-pass!", confirm=None):
    return client.post(reverse("Startpages:registration"), {
        "username": username, "email": email,
        "password": password, "confirmPassword": password if confirm is None else confirm,
    })


class PagesTests(TestCase):
    def test_public_pages_render(self):
        for name in ("home", "login", "registration", "forgot_password", "password_reset_done"):
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(f"Startpages:{name}")).status_code, 200)


class RegistrationTests(TestCase):
    def test_signup_creates_user_with_email_and_logs_in(self):
        response = signup(self.client)
        self.assertRedirects(response, reverse("Startpages:login"), fetch_redirect_response=False)
        user = User.objects.get(username="ada")
        self.assertEqual(user.email, "ada@example.com")
        self.assertTrue(user.check_password("Str0ng-pass!"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_mismatched_confirmation_is_refused(self):
        response = signup(self.client, confirm="different")
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username="ada").exists())

    def test_duplicate_username_is_refused_without_error(self):
        User.objects.create_user("ada", "other@example.com", "whatever-1")
        response = signup(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "User already exists")
        self.assertEqual(User.objects.filter(username="ada").count(), 1)

    def test_duplicate_email_is_refused(self):
        User.objects.create_user("bob", "ada@example.com", "whatever-1")
        response = signup(self.client)
        self.assertContains(response, "Email already exists")
        self.assertFalse(User.objects.filter(username="ada").exists())


class LoginTests(TestCase):
    def setUp(self):
        User.objects.create_user("ada", "ada@example.com", "Str0ng-pass!")

    def test_valid_login_redirects_and_authenticates(self):
        response = self.client.post(reverse("Startpages:login"), {"username": "ada", "password": "Str0ng-pass!"})
        self.assertRedirects(response, reverse("Startpages:login"), fetch_redirect_response=False)
        self.assertIn("_auth_user_id", self.client.session)

    def test_wrong_password_shows_error(self):
        response = self.client.post(reverse("Startpages:login"), {"username": "ada", "password": "nope"})
        self.assertContains(response, "Invalid Username or Password")
        self.assertNotIn("_auth_user_id", self.client.session)


@override_settings(EMAIL_BACKEND=LOCMEM)
class PasswordResetTests(TestCase):
    def test_reset_email_reaches_a_user_who_signed_up(self):
        signup(self.client)
        self.client.logout()
        response = self.client.post(reverse("Startpages:forgot_password"), {"email": "ada@example.com"})
        self.assertRedirects(response, reverse("Startpages:password_reset_done"), fetch_redirect_response=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["ada@example.com"])


class EmailBackendTests(TestCase):
    def test_smtp_tls_verifies_certificates(self):
        import ssl
        from backend.email_backend import EmailBackend
        context = EmailBackend(host="localhost", port=587, use_tls=True).ssl_context
        self.assertTrue(context.check_hostname)
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
