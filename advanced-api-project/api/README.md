## Views Overview

- **BookListView**: Lists all books, accessible by all users (read-only).
- **BookDetailView**: Retrieves a single book by ID, accessible by all users (read-only).
- **BookCreateView**: Allows authenticated users to create new books.
- **BookUpdateView**: Allows authenticated users to update an existing book.
- **BookDeleteView**: Allows authenticated users to delete a book.

## Permissions

- Unauthenticated users can only perform read operations (GET).
- Authenticated users can create, update, and delete books.
