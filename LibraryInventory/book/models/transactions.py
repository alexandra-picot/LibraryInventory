from django.db import models
from book.models.books import Book


class Transaction(models.Model):

    SELL = 'S'
    DELIVERY = 'D'
    RENT = 'R'
    GET_BACK = 'G'
    TRANSACTION_TYPE_CHOICES = ((SELL, 'Sell'),
                                (DELIVERY, 'New Shipment'),
                                (RENT, 'Rent'),
                                (GET_BACK, 'Got back book from rent'),
                                )

    NEW = 'N'
    USED = 'U'
    BOOK_STATE_CHOICES = ((NEW, 'New'),
                          (USED, 'Used'),
                          )

    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    book_state = models.CharField(max_length=1, choices=BOOK_STATE_CHOICES)
    quantity = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        db_table = 'transactions'
