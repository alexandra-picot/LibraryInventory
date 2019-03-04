from django.db import models
from book.models.books import Book


class Transaction(models.Model):
    NEW = 'N'
    USED = 'U'
    BOOK_STATE_CHOICES = ((NEW, 'New'),
                          (USED, 'Used'),
                          )

    quantity = models.IntegerField()
    book_state = models.CharField(max_length=1, choices=BOOK_STATE_CHOICES)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'transactions'
