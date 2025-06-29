from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):
    def setUp(self):
        self.response = self.client.get(reverse("home"))

    def test_url_exists_and_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        self.url = reverse("about")
        self.response = self.client.get(self.url)

    def test_url_exists_and_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "about.html")

    def test_aboutpage_resolves_aboutpageview(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
