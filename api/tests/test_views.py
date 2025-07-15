from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book

class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        Book.objects.create(
            title="Demo",
            description="Description",
            author="Author"
        )
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body == [
            {
                "title":Book.title,
                "description":Book.description,
                "author":Book.author,
                "created_at":Book.created_at
            }
        ]