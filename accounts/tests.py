from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignUpPageTests(TestCase):
    def test_url_exists_at_correct_loaction_signupview(self):
        response  = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        
    def test_signupview_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")
        
    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser10",
                "email": "testuser@example.com",
                "password1": "strongpass123",
                "password2": "strongpass123"
            }
            )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser10")
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@example.com")
        