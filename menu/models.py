from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):

    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

    class Meta:
        db_table = "menu"
    