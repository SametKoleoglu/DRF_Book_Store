from django.urls import path
from books.api.views import *

urlpatterns = [
    path("books/", BookListCreateAPIView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailAPIView.as_view(), name="book-detail"),
    path("books/<int:book_pk>/do_comment",CommentListCreateAPIView.as_view(), name="do-comment"),
    path("comments",CommentListCreateAPIView.as_view(), name="comments"),
    path("comments/<int:pk>/",CommentDetailAPIView.as_view(), name="comment-detail"),
]
