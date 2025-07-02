from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "book_list"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = "books.special_status"
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"
