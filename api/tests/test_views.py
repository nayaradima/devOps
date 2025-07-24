from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from api.serializers import BookSerializer

class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        Book.objects.create(
            title="Demo",
            description="Description",
            author="Author"
        )
        books = Book.objects.all()
        
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        
        #serialize the book instance
        expected_data = BookSerializer(books, many=True).data
        
        #compare against actual response
        assert response.json() == expected_data
        