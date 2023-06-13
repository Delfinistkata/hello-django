"""
Module: admin.py
Description: This module registers the Item model in the Django admin site.
"""

from django.contrib import admin
from .models import Item


# Register your models here.
admin.site.register(Item)
