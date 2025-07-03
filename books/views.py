from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

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


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_filtered_books(self, query):
        query = SearchQuery(query)
        vector = SearchVector("title", "author")
        rank = SearchRank(vector, query)
        return Book.objects.annotate(rank=rank).order_by("-rank")

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            filtered_books = self.get_filtered_books(query)
            if filtered_books.exists():
                return filtered_books

        return Book.objects.none()
