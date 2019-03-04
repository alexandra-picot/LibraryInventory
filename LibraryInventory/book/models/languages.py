from django.db import models


class Language(models.Model):
    id = models.CharField(primary_key=True, max_length=100)

    class Meta:
        db_table = 'languages'
