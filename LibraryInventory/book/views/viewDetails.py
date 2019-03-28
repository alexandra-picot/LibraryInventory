from django.views import generic
from book.models import Book

class DetailsView(generic.DetailView):
    model = Book
    template_name = 'book/details.html'

    def get_queryset(self):
        """
        Returns all details regarding Book title chosen.
        """
        return Book.object.filter(id=id)