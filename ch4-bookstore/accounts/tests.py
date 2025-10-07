from django.contrib.auth import get_user_model
from django.urls import reverse
from .forms import CustomUserCreationForm

from .views import SignUpPageView

from django.test import TestCase


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.check_password("testpassword"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="adminuser",
            email="adminuser@example.com",
            password="adminpassword",
        )
        self.assertEqual(admin_user.username, "adminuser")
        self.assertEqual(admin_user.email, "adminuser@example.com")
        self.assertTrue(admin_user.check_password("adminpassword"))
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpViewTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign up")
        self.assertNotContains(self.response, "Hi there! I should not be on the page.")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = self.response.context.get("view")
        self.assertEqual(view.__class__, SignUpPageView)
