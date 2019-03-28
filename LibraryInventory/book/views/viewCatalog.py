from django.views import generic
from book.models import Book


class CatalogView(generic.ListView):
    template_name = 'book/catalog.html'
    context_object_name = 'list_of_books'

    def get_queryset(self):
        'Return all books in catalog'

        return Book.objects.all()