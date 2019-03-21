from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, Sum
from book.models.books import Book
from book.ModelValidators import validate_nonzero


class Transaction(models.Model):
    """
    Class that correspond to the `transactions` SQL table.
    This class contains all the information about one book, and useful methods
    """

    def clean(self):
        """

        :return:
        """
        if self.type == self.SELL or self.type == self.RENT:
            book_left = self.get_quantity_for_book(self.book, self.book_state)
            if book_left - self.quantity < 0:
                raise ValidationError(message="There is not enough book available." +
                                              "Quantity asked: %(quantity)d, Books left: %(left)d",
                                      params={'quantity': self.quantity, 'left': book_left},)


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
    TRANSACTION_TYPE_CHOICES_DICT = {SELL: 'Sell',
                                     DELIVERY: 'New Shipment',
                                     RENT: 'Rent',
                                     GET_BACK: 'Got back book from rent',
    }

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
    quantity = models.IntegerField(validators=[validate_nonzero], help_text="Quantity must be greater than zero")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """
        Meta class used by Django if we need to override basic Django behaviors
        """

        # Override the table's name to the given one below
        db_table = 'transactions'

    # TODO: Test this method, handle EBOOK case
    def get_quantity_for_book(self, book_id, state=NEW):
        """

        :param book_id: the book of which we want to know the quantity left
        :param state: NEW or USED, the quantity of book left with this state
        :return: integer, the number of books left
        """
        t = Transaction.objects.filter(book=book_id, book_state=state)
        a = t.filter(Q(type__exact=self.DELIVERY) | Q(type__exact=self.GET_BACK)).aggregate(sum=Sum('quantity'))
        b = t.filter(Q(type__exact=self.SELL) | Q(type__exact=self.RENT)).aggregate(sum=Sum('quantity'))
        if not a['sum']:
            return 0
        elif not b['sum']:
            return a['sum']
        return a['sum'] - b['sum']

    def __str__(self):
        """

        :return:
        """
        return self.book.title + ", " + self.TRANSACTION_TYPE_CHOICES_DICT[self.type]
