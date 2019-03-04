from django.db import models
from book.models.editors import Editor
from book.models.genres import Genre
from book.models.authors import Author


# Create your models here.
class Book(models.Model):

    # TODO: ISBN Validator

    isbn10 = models.CharField(max_length=20)
    isbn13 = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    language = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    genre_id = models.ForeignKey(Genre, on_delete=models.PROTECT)
    editor_id = models.ForeignKey(Editor, on_delete=models.PROTECT)
    price_new = models.IntegerField()
    price_used = models.IntegerField(null=True)
    authors = models.ManyToManyField(Author)

    class Meta:
        db_table = 'books'
        unique_together = (('isbn10', 'isbn13'),)
