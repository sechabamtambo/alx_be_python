class Book:
    """Class representing a book."""

    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                return

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                return

    def list_available_books(self):
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
