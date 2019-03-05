from django.db import models


class Language(models.Model):
    """
    Class that correspond to the `languages` SQL table.
    This class contains all the information about one book, and useful methods
    """

    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        db_table = 'languages'

    def __str__(self):
        """
        :return: str, the languages id (the id is the language's name (e.g. French))
        """
        return self.id
