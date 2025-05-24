class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def show_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return f"Title: {b.title}, Author: {b.author}, ISBN: {b.isbn}"
        return "Book not found"

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

# --- Testing ---

# Create some books
book1 = Book("Python Programming", "John Doe", "1234567890")
book2 = Book("Java Programming", "Jane Doe", "9876543210")

# Create library and add books
library = Library([book1])
library.add_book(book2)

# Show a book
print(library.show_book("9876543210"))
# print(library.show_book("0000000000"))  # Book not found

# Create member
member1 = Member("Ali")
member1.borrow_book(book2)
member1.return_book(book1)
