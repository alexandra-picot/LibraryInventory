from django.db import models


class Genre(models.Model):
    id = models.CharField(primary_key=True, max_length=50, verbose_name="Genre name")

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.id