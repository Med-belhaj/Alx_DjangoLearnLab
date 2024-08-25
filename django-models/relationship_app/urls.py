from .views import list_books
from django.urls import path
from .views import LoginView, LogoutView, RegisterView
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.home, name='home'),  # Root view
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('library/<int:pk>/', views.library_detail, name='library_detail'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]
