from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book", author="Test Author", price=19.99
        )

    def test_book_listing(self):
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.price, 19.99)

    def test_book_list_view(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertTemplateUsed(response, "books/book_list.html")

    def test_book_detail_view(self):
        response = self.client.get(reverse("book_detail", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        no_response = self.client.get("/books/invalid-id/")
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.book.title)
        self.assertTemplateUsed(response, "books/book_detail.html")
