from django.contrib import admin
from books.models import Book, Comment

admin.site.register(Book)
admin.site.register(Comment)
