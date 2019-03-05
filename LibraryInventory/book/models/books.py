from django.db import models
from book.models.publishers import Publisher
from book.models.genres import Genre
from book.models.authors import Author
from book.models.languages import Language


# Create your models here.
class Book(models.Model):

    # TODO: ISBN Validator

    isbn10 = models.CharField(max_length=20, unique=True)
    isbn13 = models.CharField(max_length=20, unique=True, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    release_date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    price_new = models.IntegerField()
    price_used = models.IntegerField(null=True, blank=True)
    price_ebook = models.IntegerField(null=True, blank=True)
    rent_new = models.IntegerField(null=True, blank=True)
    rent_used = models.IntegerField(null=True, blank=True)
    rent_ebook = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'books'
        unique_together = (('isbn10', 'isbn13'),)

    def __str__(self):
        return self.title

    def get_authors_string(self):
        return ", ".join([str(author) for author in self.authors.all()])
    get_authors_string.short_description = "Author(s)"

