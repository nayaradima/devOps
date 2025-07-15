from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response   
from rest_framework import status  
from .models import Book
from .serializers import BookSerializer


# Create your views here.
# Book Resource
# /api/books

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 
        
                
        
book_view = BookView.as_view()

