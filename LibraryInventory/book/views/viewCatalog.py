from django.views import generic
from book.models import Book


class CatalogView(generic.ListView):
    template_name = 'book/catalog.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        """
        :return: Return all books from database
        """
        return Book.objects.all()