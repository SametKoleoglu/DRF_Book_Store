from django.shortcuts import get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from books.models import *
from books.api.serializers import *
from books.api.permissions import *
from rest_framework import permissions
from books.api.pagination import *


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        book_pk = self.kwargs.get("book_pk")
        book = get_object_or_404(Book, pk=book_pk)
        commentor = self.request.user
        comments = book.comments.filter(book=book, commentor=commentor)
        if comments.exists():
            raise ValidationError(
                "You have already commented this book"
            )
        serializer.save(book=book, commentor=commentor)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CommenterOrReadOnly]

    # def perform_update(self, serializer):
    #     logged_in_user = self.request.user
    #     commenter = Comment.objects.filter(commenter=logged_in_user)
    #     if logged_in_user.exists():
    #         raise ValidationError(
    #             "You can't update this comment"
    #         )
    #     serializer.save()


# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


#     # All Books
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


#     # Create Book
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
