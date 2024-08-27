from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Book

@permission_required('app_name.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # View logic to edit the book
    pass

@permission_required('app_name.can_create', raise_exception=True)
def create_book(request):
    # View logic to create a new book
    pass

@permission_required('app_name.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # View logic to delete a book
    pass
