from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# Book Resource
# /api/books

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "hello":"django"
            }
        )
        
        
book_view = BookView.as_view()

