"""
This module defines a Django form for the Item model.

Import Statements:
    - from django import forms: Imports the forms module from the Django framework.
    - from .models import Item: Imports the Item model from the current package.

Note: The Item model should be defined in a separate module within the same package.
"""

from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    """
    A form class for creating or updating instances of the Item model.

    Attributes:
        Meta:
            An inner class that provides metadata about the form.
            - model: The model class associated with the form.
            - fields: The fields of the model that should be included in the form.
            - widgets (optional): A dictionary of field names and widget instances
              that specify the custom widgets to use for rendering the form inputs.
    """

    class Meta:
        """
        Metadata class for the ItemForm.

        Attributes:
            model: The model class associated with the form.
            fields: The fields of the model that should be included in the form.
        """
        model = Item
        fields = ['name', 'done']
