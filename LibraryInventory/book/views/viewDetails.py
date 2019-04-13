from django.views import generic
from book.models import Book

class DetailsView(generic.DetailView):
    model = Book
    template_name = 'book/details.html'

