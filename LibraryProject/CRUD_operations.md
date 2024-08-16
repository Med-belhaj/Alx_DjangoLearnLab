
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Book object created successfully


book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

# 1984 George Orwell 1949


book.title = "Nineteen Eighty-Four"
book.save()

# Book title updated successfully


book.delete()
# Confirm deletion
books = Book.objects.all()
print(books)

# Book deleted successfully
# Queryset should return empty
