from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book

#Concrete View
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#GenericAPIView
# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#          return self.create(request, *args, **kwargs)