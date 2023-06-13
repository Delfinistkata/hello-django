"""
Module: models.py
Description: This module defines the Item model for the application.
"""

from django.db import models

# Create your models here.


class Item(models.Model):

    """
    Model representing an item.

    This model stores information about an item,
    including its name and status of completion.

    Attributes:
        name (CharField): The name of the item.
        done (BooleanField): The status of completion of the item.

    Methods:
        __str__(): Returns the string representation of the item.
    """

    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
