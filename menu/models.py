from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Menu(models.Model):

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)


    class Meta:
        db_table = "menu"
    