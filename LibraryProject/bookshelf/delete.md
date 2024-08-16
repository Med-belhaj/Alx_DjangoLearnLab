book.delete()
# Confirm deletion
books = Book.objects.all()
print(books)

# Book deleted successfully
# Queryset should return empty
