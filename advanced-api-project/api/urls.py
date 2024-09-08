from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # List all books
    path('books/', BookListView.as_view(), name='book-list'),
    
    # Retrieve a single book, update it, or delete it based on HTTP method
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # For retrieving a book (GET)
    path('books/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # For updating a book (PUT)
    path('books/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # For deleting a book (DELETE)
    
    # Create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),
]
