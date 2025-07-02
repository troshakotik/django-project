from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

from .models import Book, Review


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Harry Potter", author="JK Rowling", price="25.00"
        )
        cls.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="reviewuser@email.com",
            password="testpass123",
        )
        cls.review = Review.objects.create(
            book=cls.book,
            author=cls.user,
            review="An excellent review",
        )
        cls.special_permission = Permission.objects.get(codename="special_status")
        cls.login_url = reverse("account_login")
        cls.book_list_url = reverse("book_list")

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")

    def test_book_listview_for_logged_in_user(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "%s?next=/books/" % self.login_url)
        response = self.client.get("%s?next=/books/" % self.login_url)
        self.assertContains(response, "Войти")

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="reviewuser@email.com", password="testpass123")
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")
