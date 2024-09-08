from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        if value > 2024:  # Replace with the current year dynamically if needed
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested books serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
