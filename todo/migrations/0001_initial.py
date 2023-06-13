# pylint: disable=invalid-name
"""
Migration: 0001_initial
Generated by Django 3.2.19 on 2023-06-13 10:55

This migration creates the Item model with its corresponding fields.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    """
    Django migration class for creating the Item model.

    This migration creates the Item model with the following fields:
    - id: Auto-generated big integer field for the primary key
    - name: Character field with a maximum length of 50 characters
    - done: Boolean field representing whether the item is done or not
    """

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('done', models.BooleanField()),
            ],
        ),
    ]
