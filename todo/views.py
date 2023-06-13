"""
Module: views.py
Description: This module defines the views for the todo application.
"""

from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


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
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
