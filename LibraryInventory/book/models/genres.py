from django.db import models


class Genre(models.Model):
    """
    Class that correspond to the `genres` SQL table.
    This class contains all the information about one book, and useful methods
    """

    id = models.CharField(primary_key=True, max_length=50, verbose_name="Genre name")

    class Meta:
        """
        Meta class used by Django if we need to override basic Django behaviors
        """

        # Override the table's name to the given one below
        db_table = 'genres'

    def __str__(self):
        """
        :return: str, the genre's id (id is the genre's name (e.g. Fantasy))
        """
        return self.id
