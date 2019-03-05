from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'authors'

    def __str__(self):
        return self.first_name + ' ' + self.last_name