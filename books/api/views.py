from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from books.api.permissions import IsAdminUserOrReadOnly, IsCommentOwnerOrReadOnly
from books.api.pagination import SmallPagination, LargePagination

from books.api.serializers import BookSerializer, CommentSerializer
from books.models import Book, Comment

#Concrete View
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly] #sadece admin create işlemleri yapabilecek
    #pagination_class = SmallPagination

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly] #sadece admin detail'i update edebilecek


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


    #manipulation
    def perform_create(self, serializer):
        #path('books/<int:book_pk>/comment/',)
        book_pk = self.kwargs.get('book_pk')
        book = get_object_or_404(Book, pk=book_pk)
        user = self.request.user
        comments = Comment.objects.filter(book=book, comment_owner=user)
        if comments.exists():
            raise ValidationError("You can write on just 1 comment to book")
        serializer.save(book=book, comment_owner=user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsCommentOwnerOrReadOnly]

