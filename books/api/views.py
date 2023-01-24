from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book

class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
         return self.create(request, *args, **kwargs)