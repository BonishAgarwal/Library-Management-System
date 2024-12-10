from books import Book
from typing import Dict

class User:
    def __init__(self, id: str, name: str, contact: str):
        self.id = id
        self.name = name
        self.contact = contact
        self.issued_books: Dict[Book] = {}
    
    def get_user_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_contact(self):
        return self.contact

    def get_issues_by_books(self):
        return self.issued_books

    def get_number_of_issued_books(self):
        return len(self.issued_books)

    def add_books(self, book: Book):
        self.issued_books[book.get_book_id()] = book

    def remove_from_issued_books(self, book_id: int):
        del self.issued_books[book_id]
        