from django.db import models
from book.models.publishers import Publisher
from book.models.genres import Genre
from book.models.authors import Author
from book.models.languages import Language


# Create your models here.
class Book(models.Model):

    # TODO: ISBN Validator

    isbn10 = models.CharField(max_length=20)
    isbn13 = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    release_date = models.DateTimeField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    price_new = models.IntegerField()
    price_used = models.IntegerField(null=True)
    authors = models.ManyToManyField(Author)

    class Meta:
        db_table = 'books'
        unique_together = (('isbn10', 'isbn13'),)
