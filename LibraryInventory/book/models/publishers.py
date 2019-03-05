from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'publishers'

    def __str__(self):
        return self.name