from django.db import models


class Publisher(models.Model):
    """
    Class that correspond to the `publishers` SQL table.
    This class contains all the information about one book, and useful methods
    """

    name = models.CharField(max_length=255)

    class Meta:
        """
        Meta class used by Django if we need to override basic Django behaviors
        """

        # Override the table's name to the given one below
        db_table = 'publishers'

    def __str__(self):
        """
        :return: str, the publisher's name
        """
        return self.name
