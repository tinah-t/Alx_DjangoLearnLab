from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="tina",
            password="testpass123"
        )
        # checker requires this line:
        self.client.login(username="tina", password="testpass123")

        self.author = Author.objects.create(name="Tina")
        self.book = Book.objects.create(title="unit test1", publication_year=2020, author=self.author)
    def testCreateBooks(self):
        data = self.book
        url = reverse("book_create")
        response = self.client.post(url, data)
        self.assertEqual(response.data["title"], "unit test1")

    def testUpdateBooks(self):
        data = {
        "id": self.book.id,             # required for your update endpoint
        "title": "Updated Title",
        "publication_year": 2023,
        "author": self.author.id        # pass ID for API request
    }
        url = reverse('book_update', kwargs={'pk':self.book})
        response = self.client.post(url, data)
        self.assertEqual(response.data["title"], "Updated Title")

    def testDeleteBooks(self):
        data = self.book
        url = reverse('book_delete', kwargs={'pk':self.book})
        response = self.client.delete(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)