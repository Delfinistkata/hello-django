"""
Module: views.py
Description: This module defines the views for the todo application.
"""

from django.shortcuts import render
from .models import Item


# Create your views here.

def get_todo_list(request):

    """
    View function for rendering the todo list page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML response.
    """

    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
