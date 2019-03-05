from django.db import models
from book.models.books import Book


class Transaction(models.Model):
    """
    Class that correspond to the `transactions` SQL table.
    This class contains all the information about one book, and useful methods
    """

    # Create choices for the transaction's type
    # Those types will be the only choices the user has when selecting a transaction's type
    # NOTE: The check is not enforced at DB level but at code level
    SELL = 'S'
    DELIVERY = 'D'
    RENT = 'R'
    GET_BACK = 'G'
    TRANSACTION_TYPE_CHOICES = ((SELL, 'Sell'),
                                (DELIVERY, 'New Shipment'),
                                (RENT, 'Rent'),
                                (GET_BACK, 'Got back book from rent'),
                                )

    # Create choices for the book's state
    # Those types will be the only choices the user has when selecting a book's state
    # NOTE: The check is not enforced at DB level but at code level
    NEW = 'N'
    USED = 'U'
    EBOOK = 'E'
    BOOK_STATE_CHOICES = ((NEW, 'New'),
                          (USED, 'Used'),
                          (EBOOK, 'Ebook'),
                          )

    type = models.CharField(max_length=1, choices=TRANSACTION_TYPE_CHOICES)
    book_state = models.CharField(max_length=1, choices=BOOK_STATE_CHOICES)
    quantity = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """
        Meta class used by Django if we need to override basic Django behaviors
        """

        # Override the table's name to the given one below
        db_table = 'transactions'
