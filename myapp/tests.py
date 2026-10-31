from django.test import TestCase
from django.urls import reverse


class PageViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(
            response,
            "<h1>Hello, World! This is the home page of my Django application.</h1>",
        )

    def test_about_page(self):
        response = self.client.get(reverse("about"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(response, "<h1>About Page</h1>")
        self.assertContains(
            response,
            "<p>This is the about page of my Django application.</p>",
        )
    def test_contact_page(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/html; charset=utf-8")
        self.assertContains(response, "<h1>Contact Page</h1>")
        self.assertContains(
            response,
            "<p>This is the contact page of my Django application.</p>",
        )
