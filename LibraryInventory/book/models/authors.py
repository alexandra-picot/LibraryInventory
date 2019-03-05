from django.db import models


class Author(models.Model):
    """
    Class that correspond to the `authors` SQL table.
    This class contains all the information about one book, and useful methods
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        """
        Meta class used by Django if we need to override basic Django behaviors
        """

        # Override the table's name to the given one below
        db_table = 'authors'

    def __str__(self):
        """
        :return: str, the author's full name (first_name last_name)
        """
        return self.first_name + ' ' + self.last_name