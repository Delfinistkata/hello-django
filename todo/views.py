"""
Module: views.py
Description: This module defines the views for the todo application.
"""

from django.shortcuts import render, redirect
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


def add_item(request):
    """
    Adds a new item to the todo list.

    If the request method is POST,
    the function retrieves the item name
    and done status from the request's POST data,
    creates a new Item object with the provided name and done status,
    and redirects to the 'get_todo_list' view.
    If the request method is GET,
    the function renders the 'add_item.html' template.

    Args:
        request: Django HttpRequest object.

    Returns:
        If the request method is POST, a redirect to the 'get_todo_list' view.
        If the request method is GET,
        a Django HttpResponse object rendering the 'add_item.html' template.
    """
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')

    return render(request, 'todo/add_item.html')
