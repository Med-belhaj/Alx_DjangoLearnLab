from .views import list_books
from django.urls import path
from .views import LoginView, LogoutView, RegisterView
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Root view
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view')
    path('books/', views.list_books, name='list_books'),  # List all books
    path('books/add/', views.add_book, name='add_book'),  # URL pattern for adding a book
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),  # URL pattern for editing a book
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),  # URL pattern for deleting a book
]
